def fahrenheit_to_Celsius(f):
    f = float(f)
    return (f - 32.0) * 5.0 / 9.0

if __name__ == "__main__":
    v = input("Fahrenheit: ").strip()
    try:
        print(f"{fahrenheit_to_Celsius(v):.2f} °C")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")