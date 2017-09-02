# Pseudo Code for n = 5
# 1 = i_factorial(1)
# 1 * 2 = i_factorial(1) * 2 = i_factorial(2)
# 1 * 2 * 3 = i_factorial(2) * 3 = i_factorial(3)
# 1 * 2 * 3 * 4 = i_factorial(3) * 4 = i_factorial(4)
# 1 * 2 * 3 * 4 * 5 = i_factorial(4) * 5 = i_factorial(5)


# RECURSION
def r_factorial(n):
    if n < 0:
        raise ValueError('Only non-negative ( >= 0) arguments can be passed in this function')
    if n <= 1:
        return 1
    return n * r_factorial(n-1)


#  ITERATION
def i_factorial(n):
    if n < 0:
        raise ValueError('Only non-negative ( >= 0) arguments can be passed in this function')
    if n <= 1:
        return 1
    
    mult = n
    for i in range(n, 1, -1):
        mult *= (i-1)
    return mult

result_r = r_factorial(20)
print result_r

result_i = i_factorial(20)
print result_i

assert r_factorial(20) == i_factorial(20)

