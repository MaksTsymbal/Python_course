def count_lines(file):
    return len(file.readlines())

def count_chars(file):
    return len(file.read())

def test(name):
    with open(name, 'r') as file:
        file.seek(0)
        lines = count_lines(file)
        file.seek(0)
        chars = count_chars(file)
        print(f'Number of lines in the "{name}": {lines}, number of characters in the {name}: {chars}')

