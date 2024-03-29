"""
This week I'd like you to write a function format_ranges, that takes a list of numbers and returns a string that groups ranges of consecutive numbers together:

>>> format_ranges([1, 2, 3, 4, 5, 6, 7, 8])
'1-8'
>>> format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])
'1-3,5-8,10-11'

All runs of consecutive numbers will be collapsed into N-M ranges where N is the start of the consecutive range and M is the end.

This is sort of like the format that printers use for choosing which pages to print.

At first you can assume that all consecutive ranges of numbers will be at least 2 consecutive numbers long.

For the first bonus, I'd like you to handle ranges of individual numbers specially: they should be represented as a single number, like this:

>>> format_ranges([4])
'4'
>>> format_ranges([1, 3, 5, 6, 8])
'1,3,5-6,8'

For the second bonus, I'd like your function to work even if the given numbers are unordered:

>>> format_ranges([9, 1, 7, 3, 2, 6, 8])
'1-3,6-9'

For the third bonus, I'd like you to handle duplicate numbers specially. Whenever a number occurs more than once, it should be considered as part of a separate range of numbers.

>>> format_ranges([1, 9, 1, 7, 3, 8, 2, 4, 2, 4, 7])
'1-2,1-4,4,7,7-9'
>>> format_ranges([1, 3, 5, 6, 8])
'1,3,5-6,8'

The ranges should always be ordered by the lowest start number and then shortest range (when the start numbers are the same).
"""


def format_ranges(arr):
    # print(arr)
    sorted_arr = list(sorted(arr))
    range_str = ''
    start = sorted_arr[0]
    arr_len = len(sorted_arr)
    other_arr = []
    print(sorted_arr)

    for index, num in enumerate(sorted_arr):
        if (index == arr_len - 1):
            if start != num:
                range_str += str(start) + '-'
            range_str += str(num)
        elif (num == sorted_arr[index + 1]):
            other_arr.append(num)
        elif (num != (sorted_arr[index+1]-1)):
                if (start != num):
                    range_str += str(start) + '-'
                range_str += str(num) + ','
                start = sorted_arr[index+1]
    if (other_arr):
        range_str += ',' + format_ranges(other_arr)
    return range_str


def main():
    print(format_ranges([1, 2, 3, 4, 5, 6, 7, 8]))
    print(format_ranges([1, 2, 3, 4, 6, 7, 8, 9, 11]))
    print(format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11]))
    print(format_ranges([4]))
    print(format_ranges(iter([4, 5, 16, 17, 18, 20, 21])))
    print(format_ranges([10, 20, 10, 12, 11, 20]))


if __name__ == "__main__":
    main()
