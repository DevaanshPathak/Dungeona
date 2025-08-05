import random

class World:
    def __init__(self, seed=None):
        self.seed = seed or random.randint(0, 1_000_000)
        self.tiles = {}
        self.generate()

    def generate(self, width=200, height=100):
        random.seed(self.seed)

        for y in range(-height // 2, height // 2):
            for x in range(-width // 2, width // 2):
                # Distance from center to add more water near the middle
                dist = abs(x) + abs(y)

                r = random.random()

                if r < 0.05:
                    tile = "#"
                elif r < 0.15:
                    tile = "\""
                elif r < 0.25:
                    tile = "o"
                elif r < 0.35 and dist < 30:
                    tile = "~"
                else:
                    tile = "."

                self.tiles[(x, y)] = tile

        self.smooth_terrain()

    def get_tile_at(self, x, y):
        return self.tiles.get((x, y), ".")

    def set_tile_at(self, x, y, tile):
        self.tiles[(x, y)] = tile

    def smooth_terrain(self):
        """Smooth terrain by reinforcing neighbors."""
        def neighbors(x, y):
            return [self.tiles.get((x + dx, y + dy), ".")
                    for dx in [-1, 0, 1]
                    for dy in [-1, 0, 1]
                    if not (dx == 0 and dy == 0)]

        new_tiles = {}
        for (x, y), tile in self.tiles.items():
            n = neighbors(x, y)
            if n.count("~") > 4:
                new_tiles[(x, y)] = "~"
            elif n.count("\"") > 4:
                new_tiles[(x, y)] = "\""
            elif n.count("#") > 4:
                new_tiles[(x, y)] = "#"
            else:
                new_tiles[(x, y)] = tile

        self.tiles.update(new_tiles)
