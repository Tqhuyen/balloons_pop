import pygame

class AddImage:
    def __init__(self, file_path, pos):
        try:
            self.image = pygame.image.load(file_path).convert_alpha()
            self.image_rect = self.image.get_rect(center=pos)
        except FileNotFoundError:
            raise FileNotFoundError("The File cannot be found in the 'resources/images' folder!")

    def scale(self, scale_size):
        return pygame.transform.scale(self.image, scale_size)

    def render(self, window):
        window.blit(self.image, self.image_rect)
