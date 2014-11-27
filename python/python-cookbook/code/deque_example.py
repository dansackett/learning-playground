from collections import deque

file = 'somefile.txt'


def search(lines, pattern, history=5):
    """
    Search through lines of a file for a pattern match (like grep).
    Save a history of past 5 lines.
    """
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


with open(file) as f:
    for line, previous_lines in search(f, 'python', 5):
        for pline in previous_lines:
            print(previous_line, end='')
        print(line, end='')
        print('-' * 20)
