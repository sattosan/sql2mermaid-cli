import file
import mermaid
import typer


def main(
    input_file_path: str = typer.Option(None, "-i", "--input", help="Input file path."),
    output_file_path: str = typer.Option(None, "-o", "--output", help="Output file path."),
    markdown_flag: bool = typer.Option(False, "-m", "--md", help="Flag to output in markdown."),
) -> None:
    if not input_file_path:
        return

    try:
        sql_text = file.get_sql_text(input_file_path)
    except FileNotFoundError as e:
        print(e)
        return

    if not sql_text:
        return

    mermaid_text = mermaid.one_sql2mermaid(sql_text)
    if markdown_flag:
        mermaid_text = mermaid.format_markdown(mermaid_text)

    if output_file_path:
        file.write_file(output_file_path, mermaid_text)
        return
    print(mermaid_text)


if __name__ == "__main__":
    typer.run(main)
