# https://py.checkio.org/en/mission/second-index/
# You are given two strings, and you have to find an index
# of the second occurrence of the second string in the first one.
# Input: Two strings.
# Output: Int or None


def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    if text.count(symbol) < 2:
        return None
    return text.index(symbol, text.index(symbol) + 1)


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
