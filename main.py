a = 0

print('Wellcome to Fizz Buzz! \n Submit a number and get an answer!')

while a < 100:
    a = int(input('Number: '))
    if a % 3 == 0 and a % 5 == 0:
        print('FizzBuzz!')
    elif a % 5 == 0:
        print('Buzz!')
    elif a % 3 == 0:
        print('Fizz!')
    else:
        print(a)