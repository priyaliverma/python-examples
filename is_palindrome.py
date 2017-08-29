a = "pkafbj1483u40ue"
# print a.isalnum()
# given_string = "Madam I'm Adam"
# given_string = given_string.lower()
# print given_string
# given_string = ''.join(x for x in given_string if x.isalpha())
# print given_string
# print given_string[len(given_string)/2]
def is_palindrome(given_string):
    given_string = ''.join(x for x in given_string if x.isalnum()).lower()
    i = 0
    j = len(given_string)-1
    palindrome = True
    while i < j:
        forward_given_string = given_string[i]
        print ("forward_given_string", forward_given_string)
        backward_given_string = given_string[j]
        print ("backward_given_string", backward_given_string)
        i += 1
        j -= 1

        if forward_given_string != backward_given_string:
            palindrome = False
    return palindrome

result = is_palindrome("Madam I'm Adam")
print result