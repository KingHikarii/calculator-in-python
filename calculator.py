import time
import math

while(1):
    print()
    print("Select an operation: ")
    print("1. Addition (+) ")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (1/2)")
    print("6. Exponential (^n)")
    print("To Exit Press 0")

    response = int(input("Enter a number from 1 to 6: "))

    if response == 1:
        print("Addition selected!")
        digitA = int(input("Enter a number: "))
        digitB = int(input("Enter another number: "))
        final = digitA + digitB
        print(digitA , " + " , digitB , " = " , final)
        time.sleep(3)

    elif response == 2:
        print("Subtraction selected!")
        digitA = int(input("Enter a number: "))
        digitB = int(input("Enter another number: "))
        final = digitA - digitB
        print(digitA , " - " , digitB , " = " , final)
        time.sleep(3)

    elif response == 3:
        print("Multiplication selected!")
        digitA = int(input("Enter a number: "))
        digitB = int(input("Enter another number: "))
        final = digitA * digitB
        print(digitA , " * " , digitB , " = " , final)
        time.sleep(3)

    elif response == 4:
        print("Division selected!")
        digitA = int(input("Enter a number: "))
        digitB = int(input("Enter another number: "))
        final = digitA / digitB
        print(digitA, " / ", digitB, " = ", final)
        time.sleep(3)


    elif response == 5:
        print("Square Root selected!")
        digitA = int(input("Enter a number: "))
        final = math.sqrt(digitA)
        print("The square root of", digitA, "is", final)
        time.sleep(3)

    elif response == 6:
        print("Exponent selected!")
        digitA = int(input("Enter a number: "))
        digitB = int(input("Enter another number: "))
        final = math.pow(digitA, digitA)
        print(digitA, " to the power of ", digitB, " is ", final)
        time.sleep(3)

    elif response == 0:
        break;

