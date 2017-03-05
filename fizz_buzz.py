import sys

# Input from user or command line
if len(sys.argv) < 2:
    n = input('Enter number:')
else: n = sys.argv[1]

""" For non-numeric inputs such as 'a' (arbitrary string input causing ValueError),
    [] (an input causing TypeError), a (a random undefined identifier causing NameError)
"""
while type(n) != int:
    try:
        n = int(n)
    except (ValueError, TypeError, NameError):
        print('The program only accepts numeric values')
        sys.exit()

def fizz_buzz(num):
    if num % 15 == 0:
        print ('FizzBuzz')
    elif num % 3 == 0:
        print ('Fizz')
    elif num % 5 == 0:
        print ('Buzz')
    else:
        print (num)

for i in range(1, n+1):
    fizz_buzz(i)