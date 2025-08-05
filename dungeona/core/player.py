class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.jumping = False
        self.jump_height = 2
        self.jump_progress = 0
        self.inventory = {}  # Inventory dictionary for collecting items

    def in_water(self, world):
        """Check if the player is in water"""
        return world.get_tile(self.x, self.y) == '~'

    def move(self, direction, world):
        """Handle movement in WASD directions"""
        dx = {"a": -1, "d": 1}.get(direction, 0)
        dy = {"w": -1, "s": 1}.get(direction, 0)

        # Allow vertical movement only if in water
        new_x = self.x + dx
        new_y = self.y + dy if self.in_water(world) else self.y

        if 0 <= new_x < world.width and 0 <= new_y < world.height:
            tile = world.get_tile(new_x, new_y)
            if not world.is_solid(tile) or tile == '~':
                self.x = new_x
                self.y = new_y

    def apply_gravity(self, world):
        """Pull the player down if not jumping or swimming"""
        if self.jumping or self.in_water(world):
            return

        while not world.is_solid(world.get_tile(self.x, self.y + 1)):
            self.y += 1
            if self.y >= world.height - 1:
                break

    def jump(self, world):
        """Initiate jump if standing on a solid block"""
        if self.jumping:
            return
        if world.is_solid(world.get_tile(self.x, self.y + 1)):
            self.jumping = True
            self.jump_progress = self.jump_height

    def update_jump(self, world):
        """Progress the jump movement upward"""
        if self.jumping and self.jump_progress > 0:
            above = world.get_tile(self.x, self.y - 1)
            if not world.is_solid(above):
                self.y -= 1
                self.jump_progress -= 1
            else:
                self.jumping = False
        else:
            self.jumping = False

    def break_tile(self, world, direction):
        """Break the tile in the specified direction and collect it"""
        dx, dy = 0, 0
        if direction == "down":
            dy = 1
        elif direction == "up":
            dy = -1
        elif direction == "left":
            dx = -1
        elif direction == "right":
            dx = 1

        target_x = self.x + dx
        target_y = self.y + dy

        if 0 <= target_x < world.width and 0 <= target_y < world.height:
            tile = world.get_tile(target_x, target_y)

            # Only break dirt (^) for now
            if tile == '^':
                world.set_tile(target_x, target_y, ' ')  # remove tile
                self.inventory['dirt'] = self.inventory.get('dirt', 0) + 1
