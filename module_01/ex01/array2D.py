import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''function that takes as parameters a 2D array,
    prints its shape, and returns a
    truncated version of the array based'''
    if not isinstance(family, list):
        raise TypeError("The list isn't a list bozo")
    try:
        num = int(start)
        num = int(end)
    except ValueError:
        raise TypeError("One of the value isn't an int")
    my_array = np.array(family)
    print(f"My shape is : ({len(my_array)}, {len(my_array[0])})")
    array_result = my_array[start:end]
    print(f"My new shape is : ({len(array_result)}, {len(array_result[0])})")
    return array_result.tolist()


def main():
    '''Main for correction'''
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    try:
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except TypeError as error:
        print(error)
    return 0


if __name__ == "__main__":
    main()
