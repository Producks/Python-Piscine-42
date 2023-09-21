import numpy as np


def validate_list(height: list[int | float]) -> bool:
    '''validate the list if all values are integer or float'''
    for i in height:
        if not isinstance(i, (int, float)):
            return False
    return True


# weigth / heigth**2
def give_bmi(height: list[int | float], weight: list[int | float])\
     -> list[int | float]:
    '''Take a list of int or float and convert in into bmi'''
    if not validate_list(height) or not validate_list(weight):
        raise TypeError("Wrong type in the list")
    if len(height) != len(weight):
        raise TypeError("Length wasn't the same between 2 list")
    array_heigth = np.array(height)
    array_weight = np.array(weight)
    bmi = array_weight / array_heigth ** 2
    return [i for i in bmi]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''Check if the bmi is greater than the limit'''
    if not validate_list(bmi):
        raise TypeError("Wrong type in the list")
    return [True if i > limit else False for i in bmi]


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except TypeError as error:
        print(error)
    try:
        bmi = give_bmi(["Salut", 160], weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except TypeError as error:
        print(error)


if __name__ == "__main__":
    main()
