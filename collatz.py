
def collatz(number):                # Function Name, defined the parameter we are putting in 
    while number != 1:              #start of while loop, the condition to keep loop going.
        if number % 2 == 0:         # number is even formula
            number = number // 2    #  floor divides by 2
            print(number)
        if number % 2 == 1 and number != 1:     # if the number is odd and not equal to one the loop continues
            number = (number * 3) + 1           # multiplies number by 3 and adds 1 to product, 3x3 = 9 + 1 = 10
            print(number)
        if number == 1:                         #if the number is equal to 1 the loop ends, conditons are met.It is not even, odd but equal to 1. 
            print("You hit one!")
number = int(input("Please enter a number: "))  #asks user to input a number and converts to an integer, defines our variable. 
collatz(number)                                 # calls our function with paramter  