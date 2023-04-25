import typer

from sql2mermaid_cli import file, mermaid

app = typer.Typer()


@app.command()
def main(
    input_file_path: str = typer.Option(
        None, "-i", "--input", help="Input file path."),
    output_file_path: str = typer.Option(
        None, "-o", "--output", help="Output file path."),
    root_name: str = typer.Option("root", "-r", "--root", help="Root Name."),
    display_join: str = typer.Option(
        None, "-d", "--display", help="Select 'upper' or 'lower' case letters for displaying joined text."),
    markdown_flag: bool = typer.Option(
        False, "-m", "--md", help="Flag to output in markdown."),
):
    if not input_file_path:
        return

    sql_text = file.get_sql_text(input_file_path)
    if not sql_text:
        return

    mermaid_text = mermaid.convert(sql_text, root_name, display_join)
    if markdown_flag:
        mermaid_text = mermaid.format_markdown(mermaid_text)

    if output_file_path:
        file.write_file(output_file_path, mermaid_text)
        return
    print(mermaid_text)


if __name__ == "__main__":
    app()
