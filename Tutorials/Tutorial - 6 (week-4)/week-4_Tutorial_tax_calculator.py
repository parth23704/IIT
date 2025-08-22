if __name__ == "__main__":
    try:
        income = float(input("Enter taxable income: "))
    except ValueError:
        print("Invalid input"); raise SystemExit(1)
    tax = 0.02*income if income <= 20000 else (400 + 0.025*(income-20000) if income <= 50000 else 1150 + 0.035*(income-50000))
    print(f"Tax = ${tax:.2f}")