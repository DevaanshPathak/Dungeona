import time
from dungeona.core.player import Player
from dungeona.core.world import World
from dungeona.render.renderer import render
from dungeona.render.controls import get_key

def main():
    player = Player()
    world = World(seed="dungeona")

    while True:
        render(world, player)
        key = get_key()

        if key in ('a', 'd'):
            player.move(key, world)
        elif key == 'w':
            if player.in_water(world):
                player.move('w', world)  # swim upward
            else:
                player.jump(world)
        elif key == 's':
            if player.in_water(world):
                player.move('s', world)  # swim downward
        elif key == 'b':
            player.break_tile(world, 'down')
        elif key == 'q':
            break

        player.update_jump(world)
        player.apply_gravity(world)

        time.sleep(0.05)
