def top_k_frequent(terminos: list[str], k: int) -> list[str]:
    """
    returns the k most frequent terms, sorted by frequency from highest to lowest.
    In case of a tie, the terms are sorted in an ascending order.

    e.g.
    terms = ["apple", "banana", "apple", "orange", "banana", "apple"]
    top_k_frequent(terms, 2) -> ["apple", "banana"]
    apple appears 3 times, banana appears 2 times, and orange appears 1 time.
    apple is the most frequent term, followed by banana. Since k=2, we return the two most frequent terms.

    restrictions:
    - 1 <= k <= number of unique terms in the list
    """
    frequency = {}
    for term in terminos:
        frequency[term] = frequency.get(term, 0) + 1 # count the frequency of each term
    return sorted(frequency, key=lambda x: (-frequency[x], x))[:k]