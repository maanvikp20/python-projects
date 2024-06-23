from math import factorial

def print_pascals_triangle(n):
    for i in range(n):
        for j in range(n - i + 1):
            print(" ", end="")
        for j in range(i + 1):
            # nCr = n! / ((n-r)! * r!)
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
        print()

n = 10  # Change this value to the desired number of rows
print_pascals_triangle(n)
