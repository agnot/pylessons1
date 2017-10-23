def collatz(number):
    if number%2==0:
        result = number // 2
    else:
        result = 3 * number + 1
    print (result)
    return result

try:
    print('Enter number:')
    number = int(input())
    while (True):
        number = collatz(number)
        if (number == 1):
            break
except ValueError:
    print('Input value must be an integer!')

print('End of program')