import pygame

class AddText:
    def __init__(self, text, color, size, pos):
        try:
            self.font = pygame.font.Font("./src/resources/fonts/SweetUnicorn.ttf", size)
            self.text = self.font.render(text, True, pygame.Color(color))
            self.rect = self.text.get_rect(center=pos)
        except FileNotFoundError:
            raise FileNotFoundError("The File cannot be found in the 'resources/fonts' folder!")
        else:
            self.font = pygame.font.Font(None, size)

    def render(self, window):
        window.blit(self.text, self.rect)
