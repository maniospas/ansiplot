import platform


def enable_ansi():
    if platform.system() == "Windows":
        try:
            import ctypes

            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception as e:
            print(f"Could not enable ANSI on Windows: {e}")

enable_ansi()
