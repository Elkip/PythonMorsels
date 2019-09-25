"""
09/18/2019

a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of the corresponding
numbers in the two given lists-of-lists added together.

It should work something like this:
>>> matrix1 = [[1, -2], [-3, 4]]
>>> matrix2 = [[2, -1], [0, -1]]
>>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

Try to solve this exercise without using any third-party libraries

For the first bonus, modify your add function to accept and "add" any number of lists-of-lists. ✔️

>>> add([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]])
[[8, 8], [7, 7]]

For the second bonus, make sure your add function raises a ValueError if the given lists-of-lists aren't all the same shape. ✔️

>>> add([[1, 9], [7, 3]], [[1, 2], [3]])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "add.py", line 10, in add
    raise ValueError("Given matrices are not the same size.")
ValueError: Given matrices are not the same size.


"""


def add(*matrices):
    matrix_shapes = {
        tuple(len(m) for m in matrix) for matrix in matrices
    }
    if len(matrix_shapes)>1:
        raise ValueError("Given Matrices do not match")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]


matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
print(add(matrix1, matrix2))
