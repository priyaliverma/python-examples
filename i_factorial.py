def i_factorial(n):
    if n <= 0:
        raise ValueError('Only positive ( and greater than 0) arguments can be passed in this function')
    if (n == 1):
        return 1
    return n * i_factorial(n-1)

result = i_factorial(4)
print result