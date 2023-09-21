import sys


def main(argv):
    morseDict = {
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..',
        '9': '----.', ' ': '/'
    }
    if len(argv) != 2:
        print("AssertionError wrong number of arguments")
        return 1
    result = ""
    for c in argv[1]:
        if c.isalnum() or c == " ":
            result += morseDict[c.upper()]
            result += " "
        else:
            print(f"AssertionError bad character bozo {c}")
            return 1
    print(result.strip())


if __name__ == "__main__":
    main(sys.argv)
