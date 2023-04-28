<img src="https://raw.githubusercontent.com/sattosan/sql2mermaid-cli/master/img/top-image.png" width="1200px">

---

![PyPI - License](https://img.shields.io/pypi/l/sql2mermaid)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/nkato/sql2mermaid/python-tox.yml?event=push&label=pytest%20with%20py38)
![PyPI](https://img.shields.io/pypi/v/sql2mermaid)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sql2mermaid)

## sql2mermaid-cli
`sql2mermaid-cli` is a CLI tool that converts SQL query into [mermaid.js](https://mermaid.js.org/) style!.

![output-image](https://user-images.githubusercontent.com/20574756/235055268-3ecf0ec7-a3b7-45c3-93d9-fb032b14b4f6.gif)

## Required

Python >=3.8.1

## Installation

To install sql2mermaid-cli, use the following command:

```bash
$ pip install sql2mermaid-cli
```

## Getting Started

As a preparation, create a sample SQL file.

```bash
$ echo "with bar as (select * from baz)\n\
select * from foo inner join bar on foo.id = bar.id\n"> input.sql
```

The basic usage of `sql2mermaid-cli` is as follows:

```bash
$ sql2mermaid-cli -i input.sql
```

This will output the mermaid diagram to the console:

```bash
graph LR

bar([bar])
root([root])

baz[(baz)]
foo[(foo)]

bar --> baz
root --> foo
root --> bar
```

The Mermaid diagram that is outputted can be visualized on the Mermaid Live Editor website.

[Mermaid Live Editor](https://mermaid.live/)


## Options

To save the output to a file, use the -o option followed by the path to the output file:

```bash
$ sql2mermaid-cli -i input.sql -o output.txt
```

By default, the output format is plain text. To output the mermaid diagram in markdown format, use the -m option:

```bash
$ sql2mermaid-cli -i input.sql -o output.md -m
```

You can also specify either "upper" or "lower" after the -d option to display the join type of SQL in the mermaid diagram.

```bash
$ sql2mermaid-cli -i input.sql -d upper
```

This will output the mermaid diagram to the console:

```bash
graph LR

bar([bar])
foo([foo])

root[(root)]
baz[(baz)]
foo.id[(foo.id)]
bar.id[(bar.id)]

bar -- FROM --> baz
bar -- FROM --> foo
foo -- INNER JOIN --> bar
```

## Author

- [sattosan](https://github.com/sattosan)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/sattosan/sql2mermaid-cli/blob/master/LICENSE.md) for details
