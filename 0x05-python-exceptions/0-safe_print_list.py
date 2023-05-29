#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(0, x):
        try:
            print(f"{mylist[i]}", end="")
            count += 1
        except Exception:
            braek
    print()
    return count
