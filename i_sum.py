# Pseudo Code for n = 5
# 1 = i_sum(1)
# 1 + 2 = i_sum(1) + 2 = i_sum(2)
# 1 + 2 + 3 = i_sum(2) + 3 = i_sum(3)
# 1 + 2 + 3 + 4 = i_sum(3) + 4 = i_sum(4)
# 1 + 2 + 3 + 4 + 5 = i_sum(4) + 5 = i_sum(5)

def i_sum(n):
    if n <= 0:
        raise ValueError('Only positive ( and greater than 0) arguments can be passed in this function')
    if (n == 1):
        return 1
    return n + i_sum(n-1)

result = i_sum(3)
print result



