import os
import sys

def render(world, player, view_radius_x=20, view_radius_y=10):
    sys.stdout.write('\033[2J\033[H')  # Clear screen and move to top-left
    sys.stdout.flush()

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
                row += world.get_tile_at(x, y)
        print('|' + row + '|')

    print(border_top_bottom)

