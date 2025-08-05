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

        if key == 'q':
            break
        player.move(key)

if __name__ == "__main__":
    main()
