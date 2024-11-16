# Dictionary mapping colors to their corresponding values
color_codes = {
    "black": {"digit": 0, "multiplier": 1, "tolerance": None},
    "brown": {"digit": 1, "multiplier": 10, "tolerance": 1},
    "red": {"digit": 2, "multiplier": 100, "tolerance": 2},
    "orange": {"digit": 3, "multiplier": 1_000, "tolerance": None},
    "yellow": {"digit": 4, "multiplier": 10_000, "tolerance": None},
    "green": {"digit": 5, "multiplier": 100_000, "tolerance": 0.5},
    "blue": {"digit": 6, "multiplier": 1_000_000, "tolerance": 0.25},
    "violet": {"digit": 7, "multiplier": 10_000_000, "tolerance": 0.1},
    "gray": {"digit": 8, "multiplier": 100_000_000, "tolerance": 0.05},
    "white": {"digit": 9, "multiplier": None, "tolerance": None},
    "gold": {"digit": None, "multiplier": 0.1, "tolerance": 5},
    "silver": {"digit": None, "multiplier": 0.01, "tolerance": 10}
}

def calculate_resistance():
    print("Welcome to the Resistor Calculator!")
    print("Choose the number of bands:")
    print("1. 4 bands")
    print("2. 5 bands")
    print("3. 6 bands")

    try:
        choice = int(input("Enter your choice (1/2/3): "))
        if choice not in [1, 2, 3]:
            print("Invalid choice. Exiting.")
            return

        num_bands = 4 if choice == 1 else 5 if choice == 2 else 6
        print(f"\nYou selected a {num_bands}-band resistor.")

        band_colors = []
        for i in range(num_bands):
            color = input(f"Enter the color of band {i + 1}: ").strip().lower()
            if color not in color_codes:
                print(f"Invalid color '{color}'. Exiting.")
                return
            band_colors.append(color)

        # Calculate resistance
        if num_bands == 4:
            digit1 = color_codes[band_colors[0]]["digit"]
            digit2 = color_codes[band_colors[1]]["digit"]
            multiplier = color_codes[band_colors[2]]["multiplier"]
            tolerance = color_codes[band_colors[3]]["tolerance"]
            resistance = (digit1 * 10 + digit2) * multiplier
            print(f"Resistance: {resistance} ohms ± {tolerance}%")

        elif num_bands == 5:
            digit1 = color_codes[band_colors[0]]["digit"]
            digit2 = color_codes[band_colors[1]]["digit"]
            digit3 = color_codes[band_colors[2]]["digit"]
            multiplier = color_codes[band_colors[3]]["multiplier"]
            tolerance = color_codes[band_colors[4]]["tolerance"]
            resistance = (digit1 * 100 + digit2 * 10 + digit3) * multiplier
            print(f"Resistance: {resistance} ohms ± {tolerance}%")

        elif num_bands == 6:
            digit1 = color_codes[band_colors[0]]["digit"]
            digit2 = color_codes[band_colors[1]]["digit"]
            digit3 = color_codes[band_colors[2]]["digit"]
            multiplier = color_codes[band_colors[3]]["multiplier"]
            tolerance = color_codes[band_colors[4]]["tolerance"]
            temperature_coefficient = band_colors[5]
            resistance = (digit1 * 100 + digit2 * 10 + digit3) * multiplier
            print(f"Resistance: {resistance} ohms ± {tolerance}%")
            print(f"Temperature Coefficient: {temperature_coefficient}")

    except ValueError:
        print("Invalid input. Please enter numbers where required.")

if __name__ == "__main__":
    calculate_resistance()
