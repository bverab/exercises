"""
Tests for Day 2 — Merge Intervals.

Contract under test:
- Merge all overlapping intervals.
- Return the result sorted by start.
- Intervals that only touch at a border count as overlapping:
  [1, 4] & [4, 5] -> [1, 5].
- Input is NOT necessarily sorted.
- Empty input -> empty output.

Run from the repo root:  pytest week_02/test_day_02.py -v
The solution file (day_02_merge_intervals.py) must live in the same folder.
"""

import pytest

from day_02_merge_intervals import merge_intervals


def test_example_basic_overlap():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]


def test_touching_borders_merge():
    # they meet exactly at 4 -> still merge
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]


def test_nested_interval():
    # [2, 3] is fully inside [1, 4]
    assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]


def test_empty_input():
    assert merge_intervals([]) == []


def test_single_interval():
    assert merge_intervals([[5, 7]]) == [[5, 7]]


def test_unsorted_input():
    assert merge_intervals([[8, 10], [1, 3], [15, 18], [2, 6]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]


def test_one_swallows_many():
    assert merge_intervals([[1, 100], [2, 3], [4, 5], [90, 95]]) == [[1, 100]]


def test_all_identical():
    assert merge_intervals([[2, 4], [2, 4], [2, 4]]) == [[2, 4]]


def test_no_overlap_at_all():
    # gaps between all of them -> nothing merges
    assert merge_intervals([[1, 2], [3, 4], [5, 6]]) == [[1, 2], [3, 4], [5, 6]]


def test_chain_of_overlaps():
    # each overlaps the next, collapsing into a single interval
    assert merge_intervals([[1, 3], [2, 5], [4, 8], [7, 10]]) == [[1, 10]]


def test_point_intervals():
    # zero-length intervals where start == end
    assert merge_intervals([[1, 1], [1, 1], [2, 2]]) == [[1, 1], [2, 2]]