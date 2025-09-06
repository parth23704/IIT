def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def isPrime(n):
    if n <= 1:
        return False
    return (factorial(n-1) + 1) % n == 0

def main():
    num = int(input("Enter a number: "))
    if isPrime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

main()