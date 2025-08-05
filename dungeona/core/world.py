import random
from perlin_noise import PerlinNoise

class World:
    def __init__(self, width=100, height=60, seed=None):
        self.width = width
        self.height = height

        if isinstance(seed, str):
            seed = abs(hash(seed)) % (2**31)

        self.seed = seed or random.randint(0, 999999)
        self.scale = 0.1
        self.octaves = 4

        self.noise_layers = [
            PerlinNoise(octaves=2 ** i, seed=self.seed + i)
            for i in range(self.octaves)
        ]

        # Use generate_tile instead of get_tile_at
        self.tiles = [
            [self.generate_tile(x, y) for x in range(self.width)]
            for y in range(self.height)
        ]

    def generate_tile(self, x, y):
        """Generates tile based on Perlin noise terrain only once at creation."""
        nx = x * self.scale

        elevation = 0
        amplitude = 1.0
        total_amplitude = 0.0

        for noise_func in self.noise_layers:
            n = noise_func([nx])
            elevation += n * amplitude
            total_amplitude += amplitude
            amplitude *= 0.5

        elevation /= total_amplitude
        ground_y = int(elevation * 10 + 30)  # Controls terrain height center

        if y < ground_y:
            return " "  # Air
        else:
            depth = y - ground_y
            if depth > 6:
                return "^"  # Dirt / mountain
            elif depth > 4:
                return "#"  # Forest
            elif depth > 2:
                return ","  # Grass
            elif depth > 1:
                return "."  # Sand
            else:
                return "~"  # Water

    def get_tile(self, x, y):
        """Returns the current tile (after edits like digging)."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.tiles[y][x]
        else:
            return " "  # Out of bounds is air

    def set_tile(self, x, y, tile_char):
        """Sets the tile at given location to a new character."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.tiles[y][x] = tile_char

    def is_solid(self, tile):
        """Returns True if a tile blocks movement."""
        return tile not in (" ", "~")  # air and water are non-solid
