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

        if key in ('w', 'a', 's', 'd'):
            player.move(key, world)
        elif key == 'q':
            break

        player.apply_gravity(world)
