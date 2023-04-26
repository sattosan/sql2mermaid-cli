---

![PyPI - License](https://img.shields.io/pypi/l/sql2mermaid)
![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/nkato/sql2mermaid/python-tox.yml?event=push&label=pytest%20with%20py38)
![PyPI](https://img.shields.io/pypi/v/sql2mermaid)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sql2mermaid)

# sql2mermaid-cli

CLI tool for converting SQL table dependencies to [mermaid.js](https://mermaid.js.org/) style!.

# Required

Python >=3.8.1

## Installation

```bash
$ pip install sql2mermaid-cli
```

## Getting Started

Create sample sql file.

```bash
$ touch query.sql

# write sql file
$ echo "with bar as (select * from baz)\n\
select * from foo inner join bar on foo.id = bar.id\n"> query.sql
```

```bash
$ sql2mermaid-cli -i query.sql
```

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

## Options

## Author

- [sattosan](https://github.com/sattosan)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/sattosan/sql2mermaid-cli/blob/master/LICENSE.md) for details
