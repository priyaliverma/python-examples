s = 'abbbccdcccc'

print ("Given String:", s)
slow = 0
new_str = ''
prev = s[0] #a


for i in range(1, len(s)):
    # i = 1 --> 2
    print i
    if s[i] == prev and slow < i: # b != a, slow <= 1 --> b == b
        print ("in loop 1: s[i]:", s[i], "slow:", slow, "s[slow]", s[slow], "prev", prev)
        slow = i+1 #2 --> 3
        new_str += s[slow]
        slow += 1
        prev = s[i]

    elif s[i] != prev and slow <= len(s)-1:
        print("In loop 2")
        print new_str, slow
        new_str += s[slow] # a -->
        slow += 1 # 1 --> 2
        prev = s[i] # b --> b

print new_str # a
    # print i, len(s)


j = 0
s_new = ''

while j < len(s) - 1:
    if s[j] == s[j+1]:
        j += 2
        continue
    s_new += s[j]
    j += 1

if j == len(s) - 1:
    s_new += s[j]
print s_new