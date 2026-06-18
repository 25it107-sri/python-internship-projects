import math
import statistics

while True:


    print("\n===== ADVANCED CALCULATOR =====")
    
#Basic Operations
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

# Scientific Functions
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")

# Trigonometric Functions
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Cosecant")
    print("12. Secant")
    print("13. Cotangent")

# Advanced Math
    print("14. Logarithm")
    print("15. Natural Logarithm")
    print("16. Exponential")

# Matrix Operations
    print("17. Matrix Addition")
    print("18. Matrix Subtraction")
    print("19. Matrix Multiplication")
    print("20. Matrix Transpose")
    print("21. Determinant")

# Statistics
    print("22. Mean")
    print("23. Median")
    print("24. Mode")

# Number Theory
    print("25. Percentage")
    print("26. GCD")
    print("27. LCM")
    print("28. Prime Number Check")
    print("29. Fibonacci Series")


    print("30. Exit")

    choice = int(input("Choose operation: "))

#Basic Operations
    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result =", num1 + num2)

    elif choice == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result =", num1 - num2)

    elif choice == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result =", num1 * num2)

    elif choice == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Cannot divide by zero")

    
# Scientific Functions
    
    elif choice == 5:
        num1 = float(input("Enter base number: "))
        num2 = float(input("Enter exponent: "))
        print("Result =", num1 ** num2)

    elif choice == 6:
        num = float(input("Enter number: "))
        print("Square Root =", math.sqrt(num))

    elif choice == 7:
        num = int(input("Enter a positive integer: "))
        print("Factorial =", math.factorial(num))

    
# Trigonometric Functions    
    elif choice == 8:
        angle = float(input("Enter angle in degrees: "))
        radian = math.radians(angle)
        print("Sin =", round(math.sin(radian), 4))

    elif choice == 9:
        angle = float(input("Enter angle in degrees: "))
        radian = math.radians(angle)
        print("Cos =", round(math.cos(radian), 4))

    elif choice == 10:
        angle = float(input("Enter angle in degrees: "))
        radian = math.radians(angle)
        print("Tan =", round(math.tan(radian), 4))
    elif choice == 11:
        angle = float(input("Enter angle in degrees: "))
        radian = math.radians(angle)

        if math.sin(radian) != 0:
            print("Cosec =", round(1 / math.sin(radian), 4))
        else:
            print("Cosecant is undefined")
    elif choice == 12:
        angle = float(input("Enter angle in degrees: "))
        radian = math.radians(angle)

        if math.cos(radian) != 0:
            print("Sec =", round(1 / math.cos(radian), 4))
        else:
            print("Secant is undefined")
    elif choice == 13:
        angle = float(input("Enter angle in degrees: "))
        radian = math.radians(angle)

        if math.tan(radian) != 0:
            print("Cot =", round(1 / math.tan(radian), 4))
        else:
            print("Cotangent is undefined")
    
# Advanced Math        
    elif choice == 14:
        num = float(input("Enter a positive number: "))

        if num > 0:
            print("Log =", round(math.log10(num), 4))
        else:
            print("Logarithm is only defined for positive numbers")
    elif choice == 15:
        num = float(input("Enter a positive number: "))

        if num > 0:
            print("ln =", round(math.log(num), 4))
        else:
            print("Natural logarithm is only defined for positive numbers")
    elif choice == 16:
        num = float(input("Enter value of x: "))
        print("e^x =", round(math.exp(num), 4))
    
 # Matrix Operations    
    elif choice == 17:

        print("Enter Matrix A")

        a11 = int(input("A[1][1]: "))
        a12 = int(input("A[1][2]: "))
        a21 = int(input("A[2][1]: "))
        a22 = int(input("A[2][2]: "))

        print("Enter Matrix B")

        b11 = int(input("B[1][1]: "))
        b12 = int(input("B[1][2]: "))
        b21 = int(input("B[2][1]: "))
        b22 = int(input("B[2][2]: "))

        print("\nResult Matrix")

        print(a11+b11, a12+b12)
        print(a21+b21, a22+b22)
    elif choice == 18:

        print("Enter Matrix A")

        a11 = int(input("A[1][1]: "))
        a12 = int(input("A[1][2]: "))
        a21 = int(input("A[2][1]: "))
        a22 = int(input("A[2][2]: "))

        print("Enter Matrix B")

        b11 = int(input("B[1][1]: "))
        b12 = int(input("B[1][2]: "))
        b21 = int(input("B[2][1]: "))
        b22 = int(input("B[2][2]: "))

        print("\nResult Matrix")

        print(a11-b11, a12-b12)
        print(a21-b21, a22-b22)
    elif choice == 19:

        print("Enter Matrix A")

        a11 = int(input("A[1][1]: "))
        a12 = int(input("A[1][2]: "))
        a21 = int(input("A[2][1]: "))
        a22 = int(input("A[2][2]: "))

        print("Enter Matrix B")

        b11 = int(input("B[1][1]: "))
        b12 = int(input("B[1][2]: "))
        b21 = int(input("B[2][1]: "))
        b22 = int(input("B[2][2]: "))

        r11 = a11*b11 + a12*b21
        r12 = a11*b12 + a12*b22
        r21 = a21*b11 + a22*b21
        r22 = a21*b12 + a22*b22

        print("\nResult Matrix")

        print(r11, r12)
        print(r21, r22)
    elif choice == 20:

        print("Enter Matrix A")

        a11 = int(input("A[1][1]: "))
        a12 = int(input("A[1][2]: "))
        a21 = int(input("A[2][1]: "))
        a22 = int(input("A[2][2]: "))

        print("\nTranspose Matrix")

        print(a11, a21)
        print(a12, a22)
    elif choice == 21:

        print("Enter Matrix A")

        a11 = int(input("A[1][1]: "))
        a12 = int(input("A[1][2]: "))
        a21 = int(input("A[2][1]: "))
        a22 = int(input("A[2][2]: "))

        determinant = (a11 * a22) - (a12 * a21)

        print("Determinant =", determinant)
    
#Statistics
    elif choice == 22:

        numbers = list(map(float, input("Enter numbers separated by space: ").split()))

        mean = sum(numbers) / len(numbers)

        print("Mean =", mean)
    elif choice == 23:

        numbers = list(map(float, input("Enter numbers separated by space: ").split()))

        numbers.sort()

        n = len(numbers)

        if n % 2 == 0:
            median = (numbers[n//2 - 1] + numbers[n//2]) / 2
        else:
            median = numbers[n//2]

        print("Median =", median)
    elif choice == 24:

        numbers = list(map(float, input("Enter numbers separated by space: ").split()))

        print("Mode =", statistics.mode(numbers))
    
# Number Theory

    elif choice == 25:

        value = float(input("Enter value: "))
        total = float(input("Enter total: "))

        percentage = (value / total) * 100

        print("Percentage =", round(percentage, 2), "%")
    elif choice == 26:

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        print("GCD =", math.gcd(num1, num2))
    elif choice == 27:

        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        lcm = abs(num1 * num2) // math.gcd(num1, num2)

        print("LCM =", lcm)
    elif choice == 28:

        num = int(input("Enter a number: "))

        if num < 2:
            print("Not Prime")
        else:
            prime = True

            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    prime = False
                    break

            if prime:
                print("Prime Number")
            else:
                print("Not Prime")
    elif choice == 29:

        n = int(input("How many terms? "))

        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b


    elif choice == 30:
        print("Thank you for using the calculator!")
        break


else:
    print("Invalid Choice")
