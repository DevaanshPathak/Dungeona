import os
import sys
from colorama import init
init()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux/Mac

def render(world, player, view_radius_x=20, view_radius_y=10):
    clear_screen()

    # === HUD Section ===
    hud_lines = [
        f"Pos: ({player.x}, {player.y})",
        f"Tile: {world.get_tile(player.x, player.y)}",
        f"Status: {'Jumping' if player.jumping else 'Falling' if not world.is_solid(world.get_tile(player.x, player.y + 1)) else 'Standing'}",
    ]
    hud = " | ".join(hud_lines)
    print(hud)

    # === Game Viewport ===
    top = player.y - view_radius_y
    bottom = player.y + view_radius_y
    left = player.x - view_radius_x
    right = player.x + view_radius_x

    width = right - left
    border_top_bottom = '+' + ('-' * width) + '+'

    print(border_top_bottom)

    for y in range(top, bottom):
        row = ''
        for x in range(left, right):
            if x == player.x and y == player.y:
                row += '@'
            else:
                row += world.get_tile(x, y)
        print('|' + row + '|')

    print(border_top_bottom)

    # === Inventory Display ===
    if hasattr(player, 'inventory') and player.inventory:
        inventory = "Inventory: " + ", ".join(f"{k} x{v}" for k, v in player.inventory.items())
    else:
        inventory = "Inventory: (empty)"
    print(inventory)
