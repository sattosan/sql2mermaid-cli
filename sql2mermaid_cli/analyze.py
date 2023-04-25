from typing import Tuple

import sqlparse

from sql2mermaid_cli.dependencies import Dependencies, Dependency
from sql2mermaid_cli.tables import Tables


def extract_leafs(tables: Tables, dependencies: Dependencies) -> Tuple[Tables, Tables]:
    internals = Tables()
    leafs = tables.copy()
    for dep in dependencies:
        if dep.start in leafs:
            leafs.remove(dep.start)
            internals.add(dep.start)
    return internals, leafs


def analyze_query(query: str, root_name: str) -> Tuple[Tables, Dependencies]:
    tables = Tables()
    tables.add(root_name)
    dependencies = Dependencies()

    current_table = ""
    current_indent_level = 0
    is_outer_query = False

    parsed_queries = sqlparse.parse(query)
    for parsed_query in parsed_queries:
        # Get flattened tokens by parsing SQL queries.
        parsed = [x for x in parsed_query.flatten() if not _is_ignorable(x)]
        for i, token in enumerate(parsed):
            if _is_with_clause(token) or _is_create_clause(token):
                is_outer_query = True
            elif token.value == "(":
                current_indent_level += 1
            elif token.value == ")":
                current_indent_level -= 1
            elif _is_sub_query_name(token, is_outer_query, current_indent_level):
                table_name = _remove_name_quotes(token.value)
                tables.add(table_name)
                current_table = table_name
            elif _is_table_clause(token, is_outer_query, current_indent_level):
                table_name = _remove_name_quotes(parsed[i + 1].value)
                tables.add(table_name)
                current_table = table_name
            elif _is_from_or_join(token, parsed[i - 3].value):
                table_name = _remove_name_quotes(parsed[i + 1].value)
                if not table_name == "(":
                    tables.add(table_name)
                    dep = Dependency(current_table, token.value, table_name)
                    if dep not in dependencies:
                        dependencies.add(dep)
            elif _is_select_clause(token, current_indent_level):
                is_outer_query = False
                current_table = root_name

    return tables, dependencies


def _is_ignorable(x: sqlparse.sql.Token) -> bool:
    if x.ttype in (sqlparse.tokens.Newline, sqlparse.tokens.Whitespace, sqlparse.tokens.Comment):
        return True
    elif isinstance(x, sqlparse.sql.Comment) or "Comment" in str(x.ttype):
        return True
    else:
        return False


def _is_with_clause(token: sqlparse.sql.Token) -> bool:
    return token.ttype is sqlparse.tokens.Keyword.CTE


def _is_create_clause(token: sqlparse.sql.Token) -> bool:
    return token.ttype is sqlparse.tokens.Keyword.DDL


def _is_select_clause(token: sqlparse.sql.Token, indent_level: int) -> bool:
    return token.ttype is sqlparse.tokens.Keyword.DML and token.value.upper() == "SELECT" and indent_level == 0


def _is_from_or_join(token: sqlparse.sql.Token, pre_value: str) -> bool:
    if token.ttype is not sqlparse.tokens.Keyword:
        return False

    if token.value.upper() == "FROM" and not pre_value.upper() == "EXTRACT":
        return True
    elif "JOIN" in token.value.upper():
        return True
    return False


def _is_table_clause(token: sqlparse.sql.Token, is_outer_query: bool, indent_level: int) -> bool:
    return all([token.ttype is sqlparse.tokens.Keyword, token.value.upper() == "TABLE", indent_level == 0, is_outer_query])


def _is_sub_query_name(token: sqlparse.sql.Token, is_outer_query: bool, indent_level: int) -> bool:
    return all([token.ttype is sqlparse.tokens.Name, indent_level == 0, is_outer_query])


def _remove_name_quotes(name: str) -> str:
    quotes = ["`", "'", '"']
    if name[0] in quotes and name[-1] in quotes:
        return name[1:-1]
    else:
        return name
