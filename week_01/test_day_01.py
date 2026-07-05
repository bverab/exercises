"""
Tests for Day 1 — Top-K most frequent terms.

Contract under test:
- Returns the k most frequent terms.
- Ordered by frequency, descending.
- Ties are broken alphabetically, ascending.
- The result has exactly k elements (1 <= k <= number of unique terms).

Run from the repo root:  pytest week_01/test_day_01.py -v
The solution file (day_01_top_k.py) must live in the same folder.
"""

import pytest

from day_01_top_k import top_k_frequent


def test_example_from_prompt():
    terms = ["gpu", "python", "gpu", "sql", "python", "gpu", "sql", "airflow"]
    # counts -> gpu:3, python:2, sql:2, airflow:1
    assert top_k_frequent(terms, 2) == ["gpu", "python"]


def test_tie_broken_alphabetically():
    terms = ["gpu", "python", "gpu", "sql", "python", "gpu", "sql", "airflow"]
    # k=3 -> gpu(3), then python vs sql tie at 2 -> alphabetical order wins
    assert top_k_frequent(terms, 3) == ["gpu", "python", "sql"]


def test_returns_all_when_k_equals_unique_count():
    terms = ["gpu", "python", "gpu", "sql", "python", "gpu", "sql", "airflow"]
    assert top_k_frequent(terms, 4) == ["gpu", "python", "sql", "airflow"]


def test_k_one_returns_single_most_frequent():
    terms = ["a", "b", "a", "c", "a", "b"]  # a:3, b:2, c:1
    assert top_k_frequent(terms, 1) == ["a"]


def test_all_same_frequency_is_pure_alphabetical():
    terms = ["cherry", "apple", "banana"]  # all tie at 1
    assert top_k_frequent(terms, 3) == ["apple", "banana", "cherry"]


def test_single_element():
    assert top_k_frequent(["solo"], 1) == ["solo"]


def test_result_length_equals_k():
    terms = ["a", "a", "b", "b", "c", "d"]
    assert len(top_k_frequent(terms, 2)) == 2


@pytest.mark.parametrize(
    "k, expected",
    [
        (1, ["a"]),
        (2, ["a", "b"]),
        (3, ["a", "b", "c"]),
    ],
)
def test_progressive_k(k, expected):
    terms = ["a", "a", "a", "b", "b", "c"]  # a:3, b:2, c:1
    assert top_k_frequent(terms, k) == expected


def test_does_not_mutate_input():
    terms = ["x", "y", "x"]
    snapshot = list(terms)
    top_k_frequent(terms, 1)
    assert terms == snapshot