# Create your own implementation of a built-in function range, named in_range(), which takes three parameters: `start`,
# `end`, and optional step. Tips: See the documentation for `range` function

def in_range(start, end, step=1):
    current = start
    while current < end if step > 0 else current > end:
        yield current
        current += step


for i in in_range(0, 10, 2):
    print(i)



