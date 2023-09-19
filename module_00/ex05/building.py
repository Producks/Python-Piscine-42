import sys

def main(argv):
    argc = len(argv)
    if argc == 1:
        var = input("Please enter a string:\n")
    elif argc == 2:
        var = argv[1]
    else:
        print("AssetionError too many arguments")
        return 1
    print(var)
    return 0

if __name__ == "__main__":
    main(sys.argv)