from math import ceil


class float_range:

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0
        self.start, self.stop, self.step = start, stop, step

    def __len__(self):
        diff = self.stop - self.start
        # It's okay if the difference is negative, but the step must be negative too
        return max(ceil(diff / self.step), 0)

    def __iter__(self):
        i = self.start
        for _ in range(len(self)):
            yield i
            i += self.step

    def __reversed__(self):
        # Start where __iter__ ends
        i = self.start + (len(self) - 1) * self.step
        for _ in range(len(self)):
            yield i
            i -= self.step


def main():
    for i in float_range(1, 2.5, .5):
        print(i)
    for i in float_range(3.0):
        print(i)


if __name__ == "__main__":
    main()
