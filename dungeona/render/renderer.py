import os
import shutil

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def render(world, player):
    clear_screen()

    # Get terminal size with fallback
    columns, rows = shutil.get_terminal_size((80, 24))
    viewport_width = min(columns, 80) - 1   # adjust for wrapping
    viewport_height = min(rows, 24) - 1

    half_w = viewport_width // 2
    half_h = viewport_height // 2

    top = player.y - half_h
    bottom = player.y + half_h
    left = player.x - half_w
    right = player.x + half_w

    for y in range(top, bottom + 1):
        row = ""
        for x in range(left, right + 1):
            if x == player.x and y == player.y:
                row += "@"
            else:
                row += world.get_tile_at(x, y)
        print(row)
