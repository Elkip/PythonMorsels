#  write a function that returns "windows" of items from a given list.


def window(numbers, window, *, fillValue=None):
    sets = ()
    for i in numbers:
        if len(sets) < window:
            sets = sets + (i,)
        else:
            sets = sets[1:] + (i,)
        if len(sets) == window:
            yield sets
    if len(sets) < window:
        yield sets + (fillValue,) * (window - len(sets))


def main():
    num_list = [1, 2, 3, 4, 5, 6]
    print(window(num_list, 2))
    inputs = (n ** 2 for n in [1, 2, 3, 4])
    print(window(inputs, 2))


if __name__ == "__main__":
    main()
