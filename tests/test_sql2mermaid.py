from pathlib import Path

import pytest

from sql2mermaid_cli import mermaid

parent = Path(__file__).parent


@pytest.mark.parametrize(
    ("test_case"),
    [
        ("simple_case"),
        ("normal_case"),
        ("complex_case"),
        ("case_with_extract"),
        ("create_case"),
    ],
)
def test_convert(test_case: Path) -> None:
    with open(parent / test_case / "query.sql", "r") as f:
        query = f.read()
    with open(parent / test_case / "expected.txt", "r") as f:
        expected = f.read()

    got = mermaid.convert(query)
    print(got)
    assert got == expected


@pytest.mark.parametrize(
    ("test_case"),
    [
        ("simple_case"),
        ("normal_case"),
        ("complex_case"),
    ],
)
def test_convert_with_upper(test_case: Path) -> None:
    with open(parent / test_case / "query.sql", "r") as f:
        query = f.read()
    with open(parent / test_case / "expected_with_upper.txt", "r") as f:
        expected = f.read()

    got = mermaid.convert(query, root_name="changed_root_name", display_join="upper")
    assert got == expected


@pytest.mark.parametrize(
    ("test_case"),
    [
        ("simple_case"),
        ("normal_case"),
        ("complex_case"),
    ],
)
def test_convert_with_lower(test_case: Path) -> None:
    with open(parent / test_case / "query.sql", "r") as f:
        query = f.read()
    with open(parent / test_case / "expected_with_lower.txt", "r") as f:
        expected = f.read()

    got = mermaid.convert(query, root_name="changed_root_name", display_join="lower")
    assert got == expected
