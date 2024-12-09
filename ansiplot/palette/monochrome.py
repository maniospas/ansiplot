class Monochrome:
    """ANSI codes and symbols for color-blind accessible color schemes."""

    xaxis = "▬"
    yaxis = "▎"
    separator = "▕▎"
    block = "█"

    symbols = "*-+xo□◇#@%&|\\/=atevnqpbdczuij"

    # Monochromacy (Total color blindness) - grayscale scheme
    colors = [
        "\033[38;5;240m",  # Dark Gray
        "\033[38;5;244m",  # Medium Gray
        "\033[38;5;248m",  # Light Gray
        "\033[38;5;252m",  # Very Light Gray
        "\033[38;5;255m",  # Almost White
        "\033[38;5;251m",  # Off-White
        "\033[38;5;250m",  # Silver
    ]

    # Reset color to white
    # reset_color = "\033[97m"
    reset_color = "\033[0m"
