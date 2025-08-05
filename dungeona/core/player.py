class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'w':
            self.y -= 1
        elif direction == 's':
            self.y += 1
        elif direction == 'a':
            self.x -= 1
        elif direction == 'd':
            self.x += 1
