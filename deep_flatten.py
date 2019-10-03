"""
This week we're going to work on flattening iterables. I'd like to you write a function deep_flatten that accepts a list
of lists (or lists of tuples and lists) and returns a flattened version of that list of lists.

It should work like this:

>>> deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
[1, 2, 3, 4, 5, 6, 7, 8]
>>> deep_flatten([[1, [2, 3]], 4, 5])
[1, 2, 3, 4, 5]

In the examples above, we're returning a list. Your deep_flatten function should return an iterable, not necessarily a
list.

Your deep_flatten function can assume that no strings will be passed to it. We'll deal with strings later.

For the first bonus, I'd like you to make sure your deep_flatten function accepts not just lists and tuples, but
 generators, sets, and other iterable data structures (but don't worry about strings yet). ✔️

>>> sorted(deep_flatten({(1, 2), (3, 4), (5, 6), (7, 8)})
[1, 2, 3, 4, 5, 6, 7, 8]

For the second bonus, I'd like you to make deep_flatten return an iterator ✔️:

>>> flattened = deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])
>>> next(flattened)
1

For the third bonus, I'd like you to make sure deep_flatten works with strings ✔️:

>>> list(deep_flatten([['apple', 'pickle'], ['pear', 'avocado']]))
['apple', 'pickle', 'pear', 'avocado']

"""


def deep_flatten(iterable):
    flat = []
    for item in iterable:
        if type(item) in [list, tuple]:
            for i in deep_flatten(item):
                flat.append(i)
        else:
            flat.append(item)
    return flat


def main():
    print(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]]))
    deep_flatten([[1, [2, 3]], 4, 5])


if __name__ == "__main__":
    main()