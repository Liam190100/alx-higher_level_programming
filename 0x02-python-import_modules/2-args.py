#!/usr/bin/python3
if __name__ == "__main__":
    """Print list of arguments."""
    import sys

    num = len(sys.argv) - 1
    if num == 0:
        print("0 argv.")
    elif num == 1:
        print("0 argv:")
    else:
        print("{} argv:".format(num))
    for i in range(num):
        print("{}: {}".format(a + 1, sys.argv[a + 1]))

