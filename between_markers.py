# https://py.checkio.org/en/mission/between-markers/

def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    start_idx = text.find(begin)
    start_idx = 0 if start_idx == -1 else start_idx + len(begin)
    end_idx = text.find(end)
    if end_idx == -1:
        return text[start_idx:]
    return text[start_idx:end_idx]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')