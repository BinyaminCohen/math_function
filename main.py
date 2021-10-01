def pow(x, y):
    if y == 0:
        return 1
    elif y > 0:
        res = x
        for i in range(1, y):
            res *= x
        return res
    elif y < 0 and x != 0:
        res = 1 / x
        for i in (y, -1):
            res *= 1 / x
        return res


def factorial(x):
    if x < 0:
        return ("Error neg number!")
    res = 1
    for i in range(2, x + 1):
        res *= i
    return res


if __name__ == '__main__':
    print(pow(2, -2))
    print(factorial(6))
