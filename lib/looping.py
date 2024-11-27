#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    x = 10
    while(x > -1):
        print(x) if x != 0 else print('Happy New Year!')
        x-=1


def square_integers(int_list):
    # code goes here!
    return [ints*ints for ints in int_list ]

def fizzbuzz():
    # code goes here!
    for number in range(100):
        number+=1
        if(number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz")
        elif(number % 3 == 0):
            print('Fizz')
        elif(number % 5 == 0):
            print('Buzz')
        else:
            print(number)