import math

def ceil(x):
    return math.ceil(x)

def cost(weight):
    ounces = ceil(weight)
    if ounces <= 1:
        return 0.05
    else:
        return 0.05 + (ounces - 1) * 0.10

def main():
    weight = float(input("Enter the number of ounces: "))
    print(f"Cost: ${cost(weight):.2f}")

main()