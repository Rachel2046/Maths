# Knuth-Morris-Pratt algorithm
def longest_prefix_suffix(pattern: str):
    p, i = 0, 1
    m = len(pattern)
    lps = [0] * m
    while i < m:
        if pattern[i] == pattern[p]:  # matched
            lps[i] = p + 1
            p += 1
            i += 1
        elif p == 0:  # mismatched, shift pattern by 1, compare from the start of pattern
            lps[i] = 0  # no self similarity
            i += 1
        else:
            p = lps[p-1]  # mismatched, shift pattern by (m - self similarity), skip comparison of matched prefix

    return lps

def kmp(pattern, text, lps):
    """
    >>> kmp("AABAABA", "AAACABAABAABACBC", longest_prefix_suffix("AABAABA"))
    [6]
    >>> kmp("example", "This example is just another example of the current example!", longest_prefix_suffix("example"))
    [5, 29, 52]
    >>> kmp("no match", "There's no way you can match this!", longest_prefix_suffix("no match"))
    []
    """
    i, j = 0, 0
    m, n = len(pattern), len(text)
    match_at = []
    while i < n:
        if text[i] == pattern[j]:  # matched
            i += 1
            j += 1
        elif j == 0:  # mismatched, shift pattern by 1, compare from the start of pattern
            i += 1
        else:
            j = lps[j-1]  # mismatched, shift pattern by (m - self similarity), skip comparison of matched prefix
        if j == m:  # found and record a match
            match_at.append(i - m)
            j = lps[j-1]  # searching for the next match
    return match_at

