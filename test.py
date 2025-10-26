import math

def sakura_bloom(radius: float) -> list:
    """Generate soft pink petals around a circle."""
    petals = []
    for angle in range(0, 360, 45):
        x = round(radius * math.cos(math.radians(angle)), 2)
        y = round(radius * math.sin(math.radians(angle)), 2)
        petals.append((x, y))
    return petals

if __name__ == "__main__":
    petals = sakura_bloom(5)
    for i, p in enumerate(petals, 1):
        print(f"Petal {i}: {p}")