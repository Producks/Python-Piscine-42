import sys
from string import punctuation

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
    print(sum(1 for c in message if c.isupper()), "upper letters")
    print(sum(1 for c in message if c.islower()), "lower letters")
    print(sum(1 for c in message if c in punctuation), "punctuation marks")
    print(sum(1 for c in message if c.isspace()), "spaces")
    print(sum(1 for c in message if c.isdigit()), "digits")
    return 0

if __name__ == "__main__":
    main(sys.argv)