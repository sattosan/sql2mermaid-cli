TABLE_DELIMIT = "_dot_"


def _sql_format(sql_text: str) -> str:
    sql_text = sql_text.replace("${", "")
    sql_text = sql_text.replace("}", "")
    sql_text = sql_text.replace("_SESSION.", "")
    sql_text = sql_text.replace(".", TABLE_DELIMIT)

    return sql_text


def get_sql_text(path: str) -> str:
    sql_text = open(path).read()

    return _sql_format(sql_text)


def partial_repair(sql_text: str) -> str:
    return sql_text.replace(TABLE_DELIMIT, ".")


def write_file(path: str, text: str) -> None:
    open(path, "w").write(text)
