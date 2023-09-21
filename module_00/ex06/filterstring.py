from ft_filter import ft_filter
import sys


def main(argv):
    if len(argv) != 3:
        print("AssertionError wrong number of arguments")
        return 1
    try:
        num = int(argv[2])
    except ValueError:
        print("AssertionError argument wasn't a number")
        return 1
    ft_list = argv[1].split(" ")
    iterator = ft_filter(lambda str: len(str) > num, ft_list)
    for str in iterator:
        print(str)

if __name__ == "__main__":
    main(sys.argv)
