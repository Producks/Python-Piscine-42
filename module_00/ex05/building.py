import sys


def main(argv):
    '''Main function bozo'''
    argc = len(argv)
    if argc == 1:
        message = input("Please enter a string:\n")
    elif argc == 2:
        message = argv[1]
    else:
        print("AssetionError too many arguments")
        return 1
    total = upper = lower = bozo = spaces = digits = 0
    for i in message:
        total += 1
        if i.isupper() is True:
            upper += 1
        elif i.islower() is True:
            lower += 1
        elif i in ["!", "\"", "'", ",", "-", ".", ":", ";", "\n"]:
            bozo += 1
        elif i.isspace() is True:
            spaces += 1
        elif i.isdigit() is True:
            digits += 1
    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{bozo} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")
    return 0


if __name__ == "__main__":
    main(sys.argv)
