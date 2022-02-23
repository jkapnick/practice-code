# Your job is to implement a function which returns the last digit of an integer as a list.

n = 3456789
d = 0

def last_digit(n, d):
    length = len(str(n))
    num_list = []
    if d <= 0:
        num_list = []
    elif d >= length:
        d = length
        while d >= 1:
            num_list.append(int(str(n)[length - d]))
            d = d - 1
    else:
        while d >= 1:
            num_list.append(int(str(n)[length - d]))
            d = d - 1

    return num_list

print(last_digit(n, d))