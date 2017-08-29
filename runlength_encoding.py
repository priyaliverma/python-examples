given_string_to_encode = "aaeeeabbddccccaaaa"
encoded_string = []
count = 0
pointer = 0
encoded_string.append(given_string_to_encode[pointer])
for i in range(len(given_string_to_encode)):
    # print i
    if given_string_to_encode[i] == given_string_to_encode[pointer]:
        count += 1
    elif given_string_to_encode[i] != given_string_to_encode[pointer]:
        pointer = i
        encoded_string.append(count)
        count = 1
        encoded_string.append(given_string_to_encode[pointer])

    if i == len(given_string_to_encode) - 1:
        encoded_string.append(count)

print given_string_to_encode
print encoded_string

given_string_to_decode = "a4b3c5"
# given_string_to_decode = given_string_to_decode.split()
# print given_string_to_decode[2]
decoded_string = []
for i in range(len(given_string_to_decode)):
    # print i
    if not given_string_to_decode[i].isdigit():
        decoded_string.append(given_string_to_decode[i])
        # print ("Decoded string and given string[i]:",decoded_string, given_string_to_decode[i])

    elif given_string_to_decode[i].isdigit():
        number = int(given_string_to_decode[i])
        # print ("Type:",type(number))
        for j in range(number-1):
            # print("i inside number:", j)
            decoded_string.append(given_string_to_decode[i-1])
            # print("Decode when number:", decoded_string)

print given_string_to_decode
print decoded_string



