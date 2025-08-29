# 🎬 Movie Theatre Ticket Sales Simulator

# Part A — Movies catalog
movies = {
    "Dune": 12.5,
    "Barbie": 11.0,
    "Oppenheimer": 13.0,
    "Spirited Away": 10.0
}

purchases = []  # list of (title, qty, price_each, line_total)

# --- Helper functions for Part D ---
def apply_group_discount(qty, price_each):
    """10% off if buying 4 or more tickets in one purchase line"""
    subtotal = qty * price_each
    if qty >= 4:
        subtotal *= 0.9   # 10% off
    return subtotal

def apply_member_discount(total, is_member):
    """5% off the entire bill if member"""
    return total * 0.95 if is_member else total


# ======================
# Part A — Input loop
# ======================
while True:
    title = input("Enter movie title (or 'done' to finish): ")

    if title.lower() == "done":
        break

    if title not in movies:
        print("❌ Movie not found. Available:", ", ".join(movies.keys()))
        continue

    try:
        qty = int(input("Enter quantity: "))
        if qty <= 0:
            print("Quantity must be positive!")
            continue
    except ValueError:
        print("❌ Invalid quantity, please enter a number.")
        continue

    price_each = movies[title]
    line_total = apply_group_discount(qty, price_each)
    purchases.append((title, qty, price_each, line_total))

print("\n--- Receipt ---")
grand_total = 0

# ======================
# Part B — Receipt
# ======================
for title, qty, price_each, line_total in purchases:
    print(f"{title:15} x{qty:<2} @ ${price_each:<5.2f} = ${line_total:.2f}")
    grand_total += line_total

# Ask for membership discount
is_member = input("\nDo you have a member code? (y/n): ").lower() == "y"
grand_total = apply_member_discount(grand_total, is_member)

print(f"\nTotal: ${grand_total:.2f}")

# ======================
# Part C — Sales Summary
# ======================
tickets_by_movie = {}
revenue_by_movie = {}

for title, qty, price_each, line_total in purchases:
    tickets_by_movie[title] = tickets_by_movie.get(title, 0) + qty
    revenue_by_movie[title] = revenue_by_movie.get(title, 0) + line_total

print("\n--- Sales Summary ---")
for title in movies.keys():
    tix = tickets_by_movie.get(title, 0)
    rev = revenue_by_movie.get(title, 0)
    print(f"{title:15} Tickets: {tix:<3}  Revenue: ${rev:.2f}")

# ======================
# Part E — Analytics
# ======================
# Top-selling movie by tickets
top_title, top_qty = None, -1
for title, qty in tickets_by_movie.items():
    if qty > top_qty:
        top_title, top_qty = title, qty
print(f"\n🎟️ Top seller: {top_title} ({top_qty} tickets)")

# Sort by revenue
sorted_by_rev = sorted(revenue_by_movie.items(), key=lambda kv: kv[1], reverse=True)
print("\n💰 Movies sorted by revenue:")
for title, rev in sorted_by_rev:
    print(f"{title:15} ${rev:.2f}")

# Average tickets per purchase
total_tickets = sum(qty for _, qty, _, _ in purchases)
avg_tickets = total_tickets / len(purchases) if purchases else 0
print(f"\n📊 Average tickets per purchase: {avg_tickets:.2f}")