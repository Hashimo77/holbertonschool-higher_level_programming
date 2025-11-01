#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list if they are integers."""
    count = 0
    for i in range(x):
        try:
            value = my_list[i]
            try:
                print("{:d}".format(value), end="")
                count += 1
            except (ValueError, TypeError):
                continue
        except IndexError:
            break
    print()
    return count
