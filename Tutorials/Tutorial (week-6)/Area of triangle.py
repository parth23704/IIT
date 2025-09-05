def area_triangle(base, height=1):
    """Return area of a triangle given base and height (height defaults to 1)."""
    return 0.5 * float(base) * float(height)

def main():
    try:
        b = input("Enter base (b): ")
        area = area_triangle(b)  # height defaults to 1
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f"Base: {float(b)}, Height: 1 -> Area = {area}")

if __name__ == "__main__":
    main()