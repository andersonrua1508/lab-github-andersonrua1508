def greet(name: str, hour: int | None = None) -> str:
    if not name or not name.strip():
        raise ValueError("name must not be empty")

    if hour is None:
        return f"Hola, {name}!"

    if not (0 <= hour <= 23):
        raise ValueError("hour must be between 0 and 23")

    if 5 <= hour <= 11:
        greeting = "Buenos días"
    elif 12 <= hour <= 18:
        greeting = "Buenas tardes"
    else:
        greeting = "Buenas noches"

    return f"{greeting}, {name}!"


if __name__ == "__main__":
    print(greet("Mundo", 8))