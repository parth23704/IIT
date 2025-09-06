def sort_planets(planets):
    # Sort by surface area (index 1), descending
    return sorted(planets, key=lambda x: x[1], reverse=True)

def main():
    # Updated planet data with corrected surface areas (in million km²)
    Planets = [
        ('Mercury', 74.8, 1),
        ('Venus', 460.2, 2),
        ('Earth', 510.1, 3),
        ('Mars', 144.8, 4),
        ('Jupiter', 61418, 5),
        ('Saturn', 42700, 6),
        ('Uranus', 8083, 7),
        ('Neptune', 7618, 8)
    ]
    
    sorted_planets = sort_planets(Planets)
    
    print("Sorted by surface area in descending order:")
    for planet in sorted_planets:
        print(planet[0], end=" ")

main()
