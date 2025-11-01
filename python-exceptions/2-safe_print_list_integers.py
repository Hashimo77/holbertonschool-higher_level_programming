#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list if they are integers."""
    count = 0
    for i in range(x):
        try:
            # Cəhd et integer çap etməyə
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Əgər integer deyilsə, sakitcə keç
            continue
        except IndexError:
            # Əgər indeks listdən böyükdürsə, dayandır
            break
    print()
    return count
