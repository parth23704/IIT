def get_input():
    old_balance = float(input("Enter old balance: "))
    charges = float(input("Enter charges for month: "))
    credits = float(input("Enter credits: "))
    return old_balance, charges, credits

def calculate_balance(old_balance, charges, credits):
    finance_charge = old_balance * 0.015
    new_balance = old_balance + charges - credits + finance_charge
    
    if new_balance <= 20:
        min_payment = new_balance
    else:
        min_payment = 20 + 0.1 * (new_balance - 20)
    
    return new_balance, min_payment

def display(new_balance, min_payment):
    print(f"New balance: ${new_balance:.2f}")
    print(f"Minimum payment: ${min_payment:.2f}")

def main():
    old_balance, charges, credits = get_input()
    new_balance, min_payment = calculate_balance(old_balance, charges, credits)
    display(new_balance, min_payment)

main()