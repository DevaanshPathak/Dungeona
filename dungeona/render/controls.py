import sys
import os

if os.name == 'nt':
    import msvcrt

    def get_key():
        ch = msvcrt.getch()
        if ch in (b'\x00', b'\xe0'):
            # Arrow keys come in two-part codes, second part tells direction
            ch2 = msvcrt.getch()
            arrows = {
                b'H': 'w',  # Up
                b'P': 's',  # Down
                b'K': 'a',  # Left
                b'M': 'd'   # Right
            }
            return arrows.get(ch2)
        else:
            return ch.decode(errors='ignore').lower()

else:
    import tty
    import termios

    def get_key():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            if ch == '\x1b':
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    arrows = {
                        'A': 'w',  # Up
                        'B': 's',  # Down
                        'D': 'a',  # Left
                        'C': 'd'   # Right
                    }
                    return arrows.get(ch3)
            return ch.lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
