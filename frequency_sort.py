# https://py.checkio.org/en/mission/sort-array-by-element-frequency/
# Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times
# they appear in elements. If two elements have the same frequency, they should end up in the same order as the first
# appearance in the iterable.
# Input: Iterable Output: Iterable


def frequency_sort(items):
    return sorted(
        items,
        key=lambda item: (items.count(item), -items.index(item)),
        reverse=True)


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")