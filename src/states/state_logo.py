import pygame
from src import commons
from src.assets.image import AddImage
from src.states.base import State
from src.states.state_menu import MainMenuState


class LogoState(State):
    def __init__(self, game):
        super(LogoState, self).__init__(game)

        # Logo
        self.logo_img = AddImage("../resources/images/Logo.png", self.game.window_rect.center)
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 3000:
            # Activate New State
            new_state = MainMenuState(self.game)
            new_state.enter_state()
            # Music
            try:
                pygame.mixer.music.load("../resources/music/relax_music.mp3")
                pygame.mixer.music.set_volume(commons.music_volume)
                pygame.mixer.music.play(-1)
            except FileNotFoundError:
                raise FileNotFoundError("The File cannot be found in the 'resources/fonts' folder!")


    def render(self, window):
        window.fill(pygame.Color("black"))
        self.logo_img.render(window)