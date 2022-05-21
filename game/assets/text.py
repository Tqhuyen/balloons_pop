import pygame

class AddText:
    def __init__(self, text, font, color, size, pos):
        try:
            self.font = pygame.font.Font(font, size)
            self.text = self.font.render(text, True, pygame.Color(color))
            self.text_rect = self.text.get_rect(center=pos)
        except FileNotFoundError:
            raise FileNotFoundError("The File cannot be found in the 'resources/fonts' folder!")

    def render(self, window):
        window.blit(self.text, self.text_rect)
