class Pretty:
    """Some pretty symbols and ansi codes for unicode reads and writes."""
    xaxis = "▬"
    yaxis = "▎"
    separator = "▕▎"
    block = "█"

    symbols = "*-+xo□◇#@%ate&gvnqdczuij"

    colors = [
        "\033[91m",  # Red
        "\033[92m",  # Green
        "\033[93m",  # Yellow
        "\033[94m",  # Blue
        "\033[95m",  # Magenta
        "\033[96m",  # Cyan
        "\033[93;1m",  # Bright Yellow
        "\033[96;1m",  # Bright Cyan
        "\033[91;1m",  # Bright Red
        "\033[92;1m",  # Bright Green
        "\033[94;1m",  # Bright Blue
        "\033[95;1m",  # Bright Magenta
        "\033[38;5;208m",  # Orange
        "\033[38;5;202m",  # Dark Orange
        "\033[38;5;198m",  # Pink
        "\033[38;5;165m",  # Purple
        "\033[38;5;34m",  # Forest Green
        "\033[38;5;70m",  # Teal
        "\033[38;5;69m",  # Aqua
        "\033[38;5;220m",  # Gold
        "\033[38;5;82m",  # Lime Green
        "\033[38;5;203m",  # Salmon
        "\033[38;5;166m",  # Coral
        "\033[38;5;99m",  # Orchid
        "\033[38;5;64m",  # Olive Green
        "\033[38;5;208;1m",  # Bright Orange
        "\033[38;5;56m",  # Dark Violet
        "\033[38;5;123m",  # Steel Blue
    ]

    reset_color = "\033[0m"
