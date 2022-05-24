import random
from src.assets.image import AddImage

class Balloon:
    def __init__(self, game, file_path, coord_x, speed):
        self.game = game
        self.speed = speed
        self.image = AddImage(file_path, (coord_x, self.game.window_rect.height - 80))

    def reset_balloon(self):
        self.image.rect.x = random.randint(80, self.game.window_rect.width - 80)
        self.image.rect.y = self.game.window_rect.height - 80
        self.speed += 1

    def update(self):
        self.image.rect.y -= self.speed
        if self.image.rect. y < 0:
            self.reset_balloon()

    def render(self, window):
        self.update()
        self.image.render(window)


