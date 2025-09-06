def get_input():
    annual_rate = float(input("Enter annual rate of interest: "))
    monthly_payment = float(input("Enter monthly payment: "))
    balance = float(input("Enter beg. of month balance: "))
    return annual_rate, monthly_payment, balance

def calculate(annual_rate, monthly_payment, balance):
    monthly_rate = annual_rate / 12 / 100
    interest = balance * monthly_rate
    reduction = monthly_payment - interest
    end_balance = balance - reduction
    return interest, reduction, end_balance

def display(interest, reduction, end_balance):
    print(f"Interest paid for the month: ${interest:.2f}")
    print(f"Reduction of principal: ${reduction:.2f}")
    print(f"End of month balance: ${end_balance:.2f}")

def main():
    annual_rate, monthly_payment, balance = get_input()
    interest, reduction, end_balance = calculate(annual_rate, monthly_payment, balance)
    display(interest, reduction, end_balance)

main()