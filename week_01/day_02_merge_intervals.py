def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Given a list of intervals, merge all overlapping intervals and return a list of the merged intervals.

    e.g.
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    merge_intervals(intervals) -> [[1, 6], [8, 10], [15, 18]]
    The first two intervals overlap and are merged into [1, 6].

    restrictions:
    - Each interval is represented as a list of two integers [start, end].
    - The input list may not be sorted.
    - The output list should be sorted by the start of each interval.
    """
    if not intervals:
        return []

    new_ranges = []
    intervals = [r[:] for r in sorted(intervals, key=lambda x: x[0])]
    for r in intervals:
        if not new_ranges:
            new_ranges.append(r)
        else:
            if r[0] <= new_ranges[-1][1]:
                new_ranges[-1][1] = max(new_ranges[-1][1], r[1])
            else:
                new_ranges.append(r)
    return new_ranges
