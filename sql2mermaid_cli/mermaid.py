from typing import Literal

from sql2mermaid_cli import analyze, file
from sql2mermaid_cli.dependencies import Dependencies
from sql2mermaid_cli.tables import Tables


def convert(query: str, root_name: str = "root", display_join: Literal["none", "upper", "lower"] = "none") -> str:
    tables, dependencies = analyze.analyze_query(query, root_name)
    internals, leafs = analyze.extract_leafs(tables, dependencies)
    mermaid_text = _generate_mermaid(
        internals, leafs, dependencies, display_join)
    return mermaid_text


def _generate_mermaid(
    internals: Tables, leafs: Tables, dependencies: Dependencies, display_join: Literal["none", "upper", "lower"]
) -> str:
    res = "graph LR\n\n"
    for table in internals:
        res += f"{table}([{table}])\n"

    res += "\n"
    for table in leafs:
        res += f"{table}[({table})]\n"

    res += "\n"
    for dep in dependencies:
        mark = ""
        if display_join == "upper":
            mark = f"-- {dep.mark.upper()} "
        elif display_join == "lower":
            mark = f"-- {dep.mark.lower()} "
        res += f"{dep.start} {mark}--> {dep.end}\n"

    res = file.partial_repair(res)
    return res


def format_markdown(text: str) -> str:
    return "```mermaid\n" + text + "```\n"
