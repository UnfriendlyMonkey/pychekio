import re
from itertools import zip_longest

def backward_string_by_word(text: str) -> str:
    # your code here
    words = [word[::-1] for word in text.split()]
    spaces = re.findall(r'[ ]+', text)
    return ''.join(w + s for w, s in zip_longest(words, spaces, fillvalue=''))


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")