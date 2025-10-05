# ---------------------------------------------------------
# Name: Parth Bhavsar
# Student ID: u3311230
# Subject: IIT
# Assignment: [2nd - Python Fundamentals] Case Study 3 - Boolean Circuit Equivalence
# Date: 17/09/2025
# ---------------------------------------------------------

def circuit_a(A, B, C):
    a = not A
    c = not C
    temp1 = not (a and c)
    b_not = not B
    e = A and b_not
    f = A and B and C
    result = e or f
    return result

def circuit_b(A, B, C):
    b_not = not B
    temp1 = b_not or C
    result = A and temp1
    return result

def main():
    A = bool(int(input("Enter A (0 or 1): ")))
    B = bool(int(input("Enter B (0 or 1): ")))
    C = bool(int(input("Enter C (0 or 1): ")))

    X = circuit_a(A, B, C)
    Y = circuit_b(A, B, C)

    print("X (Circuit A) =", int(X))
    print("Y (Circuit B) =", int(Y))

if __name__ == "__main__":
    main()
