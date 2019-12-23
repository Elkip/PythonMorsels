#  write a FuzzyString class which acts like a string, but does comparisons in a case-insensitive way.


class FuzzyString:
    def __init__(self, string):
        self.string = str(string)

    def __eq__(self, other):
        return str(self.string).lower() == str(other).lower()

    def __add__(self, other):
        return str(self.string) + str(other)

    def __str__(self):
        return self.string

    def __repr__(self):
        return "'"+self.string+"'"


def main():
    x = FuzzyString("hel1O!")
    y = "Hel1o!"
    print(x==y)
    x  = FuzzyString(2)
    y = 2
    print(x==y)


if __name__ == "__main__":
    main()
