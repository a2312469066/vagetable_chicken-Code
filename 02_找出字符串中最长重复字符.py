import itertools
def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if not line:
        return 0
    num_list = []
    for key,group in itertools.groupby(line):
        num_list.append(len(list(group)))
    num_list.sort(reverse=True)
    return num_list[0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
