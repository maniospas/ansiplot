class DeuteranopiaFriendly:
    """ANSI codes and symbols for color-blind accessible color schemes."""

    xaxis = "▬"
    yaxis = "▎"
    separator = "▕▎"
    block = "█"

    symbols = "*-+xo□◇#@%&|\\/=atevnqpbdczuij"

    # Deuteranopia-friendly color scheme
    colors = [
        "\033[38;5;214m",  # Orange
        "\033[38;5;51m",  # Turquoise
        "\033[38;5;226m",  # Bright Yellow
        "\033[38;5;21m",  # Blue
        "\033[38;5;99m",  # Violet
        "\033[38;5;159m",  # Light Cyan
        "\033[38;5;208m",  # Gold
        "\033[38;5;14m",  # Aqua
    ]

    # Reset color to white
    # reset_color = "\033[97m"
    reset_color = "\033[0m"
