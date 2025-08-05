class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.jumping = False
        self.jump_height = 2
        self.jump_progress = 0

    def in_water(self, world):
        return world.get_tile(self.x, self.y) == '~'

    def move(self, direction, world):
        dx = {"a": -1, "d": 1}.get(direction, 0)
        dy = {"w": -1, "s": 1}.get(direction, 0)

        new_x = self.x + dx
        new_y = self.y + dy if self.in_water(world) else self.y

        tile = world.get_tile(new_x, new_y)
        if not world.is_solid(tile) or tile == '~':
            self.x = new_x
            self.y = new_y

            # 🛠️ After moving, check if the player is now unsupported (falling)
            if not self.in_water(world) and not world.is_solid(world.get_tile(self.x, self.y + 1)) and not self.jumping:
                self.apply_gravity(world)


    def apply_gravity(self, world):
        if self.jumping or self.in_water(world):
            return  # Skip gravity while jumping or swimming

        while not world.is_solid(world.get_tile(self.x, self.y + 1)):
            self.y += 1
            if self.y >= world.height - 1:
                break

    def jump(self, world):
        if self.jumping:
            return  # Already jumping

        if world.is_solid(world.get_tile(self.x, self.y + 1)):
            self.jumping = True
            self.jump_progress = self.jump_height

    def update_jump(self, world):
        if self.jumping and self.jump_progress > 0:
            above = world.get_tile(self.x, self.y - 1)
            if not world.is_solid(above):
                self.y -= 1
                self.jump_progress -= 1
            else:
                self.jumping = False
        else:
            self.jumping = False

def in_water(self, world):
    return world.get_tile(self.x, self.y) == "~"