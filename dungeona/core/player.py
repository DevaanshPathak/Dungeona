class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.jumping = False
        self.jump_height = 2  # how high player can jump
        self.jump_progress = 0

    def move(self, direction, world):
        dx, dy = 0, 0
        if direction == 'a':
            dx = -1
        elif direction == 'd':
            dx = 1
        elif direction == 's':
            dy = 1

        new_x = self.x + dx
        new_y = self.y + dy

        tile = world.get_tile_at(new_x, new_y)
        if not world.is_solid(tile):
            self.x = new_x
            self.y = new_y

    def apply_gravity(self, world):
        if not self.jumping:
            while world.get_tile_at(self.x, self.y + 1) in world.air_tiles:
                self.y += 1

    def jump(self, world):
        if self.jumping:
            return  # already jumping

        # Only allow jumping if standing on solid ground
        if world.is_solid(world.get_tile_at(self.x, self.y + 1)):
            self.jumping = True
            self.jump_progress = self.jump_height

    def update_jump(self, world):
        if self.jumping and self.jump_progress > 0:
            above_tile = world.get_tile_at(self.x, self.y - 1)
            if not world.is_solid(above_tile):
                self.y -= 1
                self.jump_progress -= 1
            else:
                self.jumping = False  # blocked above
        else:
            self.jumping = False
