import sys

def main(argv):
    if len(argv) == 1:
        print("AssertionError: no argument were provided")
        return 1
    if len(argv) > 2:
        print("AssertionError: more than one argument is provided")
        return 1
    try:
        val = int(argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return 1
    if int(argv[1]) % 2 == 0:
       print("I'm Even")
    else:
        print("I'm Odd.")
if __name__ == "__main__":
    main(sys.argv)