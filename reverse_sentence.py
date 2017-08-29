# or_given_string = "Alice likes Bob"
# print or_given_string
# given_string = or_given_string.split(' ')
# # print given_string
# reversed_string = []
# for i in range (len(given_string)-1, -1, -1):
#     # print i
#     reversed_string.append(given_string[i])
# reversed = ""
# reversed += "'" + ' '.join(reversed_string) + "'"
# print reversed

given_string = "Alice likes Bob"
reversed_string = ''
# given_string = given_string.split(' ')
for i in range(len(given_string)-1, -1, -1):
    reversed_string += given_string[i]

reversed_string = list(reversed_string)
# print len(reversed_string)
start = 0
for i in range(len(reversed_string) + 1):
    if i == len(reversed_string) or reversed_string[i] == ' ':
        end = i-1
        while start < end:
            temp = reversed_string[end]
            reversed_string[end] = reversed_string[start]
            reversed_string[start] = temp
            start += 1
            end -= 1
        start = i+1
    else:
        continue
print given_string
print ''.join(reversed_string)



# reversed_string = reversed_string.split(' ')
# for i in reversed_string:
#     # print ("Check i", i[0], i[-1], len(i))
#     # print ("i",i)
#     start = 0
#     end = len(i)-1
#     i_split = i.split()
#     # print ("Start: {}, End: {}, iend: {}, type: {}".format(start, end, i[end], type(i[end])))
#     # print ("i_split:", type(i_split),i_split[0][0])
#     print type(i_split[0][0])
#     while start < end:
#         temp = i[end]
#         i[end] = i[start]
#         i[start] = temp
#         print ("temp: {}, start: {}, end: {}", temp,start, end)
#         start += 1
#         end -= 1
# print reversed_string
#         # print i[j]
#



# print reversed_string
# for i in range(len(given_string)):
#     print i