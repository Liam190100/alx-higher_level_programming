#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    
    total_sum = 0
    previous_number = 0

    for i in range(1, len(argv)):
        current_number = int(argv[i])
        total_sum = current_number + previous_number
        previous_number = total_sum
    
    print("{}".format(total_sum))

