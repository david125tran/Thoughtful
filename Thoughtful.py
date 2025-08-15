def sort(width, height, length, mass):
    """
    Sort packages into STANDARD, SPECIAL, or REJECTED stacks based on volume, dimensions, and mass.
    
    :param width: Width of the package in cm
    :param height: Height of the package in cm
    :param length: Length of the package in cm
    :param mass: Mass of the package in kg
    :return: str - one of "STANDARD", "SPECIAL", "REJECTED"
    """
    # Validate inputs without using ternary operators
    try:
        if isinstance(width, str):
            width = float(width.strip())
        else:
            width = float(width)

        if isinstance(height, str):
            height = float(height.strip())
        else:
            height = float(height)

        if isinstance(length, str):
            length = float(length.strip())
        else:
            length = float(length)

        if isinstance(mass, str):
            mass = float(mass.strip())
        else:
            mass = float(mass)

    except (TypeError, ValueError, AttributeError):
        raise ValueError("All inputs must be numeric (optionally as strings with spaces).")

    # Check for negative values and return message
    if width <= 0:
        raise ValueError("Width must be a positive number.")
    if height <= 0:
        raise ValueError("Height must be a positive number.")
    if length <= 0:
        raise ValueError("Length must be a positive number.")
    if mass <= 0:
        raise ValueError("Mass must be a positive number.")

    # Calculate volume
    volume = width * height * length

    # Check bulky criteria
    bulky = volume >= 1_000_000 or width >= 150 or height >= 150 or length >= 150

    # Check heavy criteria
    heavy = mass >= 20

    # Determine stack without ternary operators
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


# ---- Example tests ----
print(sort(100, 100, 100, 10))  # STANDARD
print(sort(200, 50, 50, 10))    # SPECIAL (bulky)
print(sort(50, 50, 50, 25))     # SPECIAL (heavy)
print(sort(200, 200, 200, 25))  # REJECTED (bulky + heavy)
print(sort(100, 100, 100, 20))  # SPECIAL (heavy)
