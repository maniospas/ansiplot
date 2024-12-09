class TritanopiaFriendly:
    """ANSI codes and symbols for color-blind accessible color schemes."""

    xaxis = "▬"
    yaxis = "▎"
    separator = "▕▎"
    block = "█"

    symbols = "*-+xo□◇#@%&|\\/=atevnqpbdczuij"

    # Tritanopia-friendly color scheme
    colors = [
        "\033[38;5;196m",  # Red
        "\033[38;5;46m",  # Green
        "\033[38;5;142m",  # Olive Green
        "\033[38;5;54m",  # Purple
        "\033[38;5;201m",  # Bright Pink
        "\033[38;5;153m",  # Light Grayish Blue
        "\033[38;5;136m",  # Brown
        "\033[38;5;21m",  # Blue
    ]

    # Reset color to white
    # reset_color = "\033[97m"
    reset_color = "\033[0m"
