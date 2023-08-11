#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) - 1

    print(f"{num_args} argument{'' if num_args == 1 else 's'}.")

    for i in range(1, len(argv)):
        print(f"{i}: {argv[i]}")

