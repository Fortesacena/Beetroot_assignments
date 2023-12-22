
def count_lines(name):
    with open(name, 'r') as file:
        nr_of_lines = len(file.readlines())
    return nr_of_lines


def count_chars(name):
    with open(name, 'r') as file:
        nr_of_chars = len(file.read())
    return nr_of_chars

def test(name):
    lines = count_lines(name)
    chars = count_chars(name)

    return f'The number of lines: {lines}\nThe number of chars: {chars}'