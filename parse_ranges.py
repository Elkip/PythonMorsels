'''
This week I'd like you to write a function called parse_ranges, which accepts a string containing ranges
 of numbers and returns an iterable of those numbers.
The numeric ranges in the string will consist of two numbers separated by hyphens and each of the ranges will
be separated by commas and any number of spaces.

Your function should work like this:

>>> parse_ranges('1-2,4-4,8-10')
[1, 2, 4, 8, 9, 10]
>>> parse_ranges('0-0, 4-8, 20, 43-45')
[0, 4, 5, 6, 7, 8, 20, 43, 44, 45]

In the examples above the functions return lists of numbers. Your function can return any iterable of
numbers that you'd like though.
'''


def parse_ranges(ranges_string):
    ranges = ranges_string.split(",")
    final = []

    for i in ranges:
        if i.find("->") != -1:
            ignore = i.split("->")[0]
            final.append(int(ignore))
        elif i.find("-") == -1:
            # yield i
            final.append(int(i))
        else:
            start, stop = i.split("-")
            for x in range(int(start), int(stop)+1):
                # yield x
                final.append(x)
    return final


'''
# A solution which returns an iterator
def parse_ranges(ranges):
    for group in ranges.split(','):
        start, sep, end = group.partition('-')
        if end.startswith('>') or not sep:
            yield int(start)
        else:
            yield from range(int(start), int(end)+1)
'''


def main():
    print(parse_ranges('0-0, 4-8, 20, 43-45'))
    print(parse_ranges('0,4-8,20->exit,43-45'))


if __name__ == '__main__':
    main()
