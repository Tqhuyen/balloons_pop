import pygame
from src.assets.image import AddImage
from src.states.base import State


class LogoState(State):
    def __init__(self, game):
        super(LogoState, self).__init__(game)

        # Logo
        self.logo_img = AddImage("../resources/images/Logo.png", self.game.window_rect.center)
        self.time_active = 0

    def update(self, dt):
        pass


    def render(self, window):
        window.fill(pygame.Color("black"))
        self.logo_img.render(window)