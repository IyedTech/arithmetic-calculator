import math
import time

def prime_factorization():
    n = int(input("Enter the number: "))
    original = n
    factors = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1

    builder = ' × '.join(str(f) for f in factors)
    print(f"{original} = {builder}")


def divisors():
    n = int(input("Enter the number: "))
    print(f"Divisors of {n}:")
    for divisor in range(1, n + 1):
        if n % divisor == 0:
            print(divisor)


def gcd_out_of_the_box():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    a_div, b_div = [], []

    for i in range(1, a + 1):
        if a % i == 0:
            a_div.append(i)
    for j in range(1, b + 1):
        if b % j == 0:
            b_div.append(j)

    common_divisors = [d for d in a_div if d in b_div]
    k = max(common_divisors)
    print(f"The GCD of {a} and {b} is: {k}")


def lcm():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = math.lcm(a, b)
    print(f"The LCM of {a} and {b} is: {result}")


def quotient_and_remainder():
    a = int(input("Enter the dividend: "))
    b = int(input("Enter the divisor: "))
    quotient = a // b
    remainder = a % b
    print(f"Quotient: {quotient}, Remainder: {remainder}")


def main():
    print("Welcome to the Arithmetic Calculator, dear student!")
    time.sleep(1)
    print("Hope you will find it useful!")
    time.sleep(1)

    while True:
        print("\n--- MENU ---")
        print("1. Prime factorization")
        print("2. Divisors of a number")
        print("3. GCD (out of the box method)")
        print("4. LCM")
        print("5. Quotient and remainder")
        print("6. Exit")

        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            prime_factorization()
        elif choice == 2:
            divisors()
        elif choice == 3:
            gcd_out_of_the_box()
        elif choice == 4:
            lcm()
        elif choice == 5:
            quotient_and_remainder()
        elif choice == 6:
            print("Goodbye, student! Keep learning and coding!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
