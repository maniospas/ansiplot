class ProtanopiaFriendly:
    """ANSI codes and symbols for color-blind accessible color schemes."""

    xaxis = "▬"
    yaxis = "▎"
    separator = "▕▎"
    block = "█"

    symbols = "*-+xo□◇#@%&|\\/=atevnqpbdczuij"

    # Protanopia-friendly color scheme
    colors = [
        "\033[38;5;172m",  # Dark Yellow
        "\033[38;5;36m",  # Cyan
        "\033[38;5;229m",  # Bright Yellow
        "\033[38;5;21m",  # Blue
        "\033[38;5;105m",  # Bluish Purple
        "\033[38;5;153m",  # Soft Blue
        "\033[38;5;220m",  # Gold
        "\033[38;5;50m",  # Forest Green
    ]

    # Reset color to white
    # reset_color = "\033[97m"
    reset_color = "\033[0m"
