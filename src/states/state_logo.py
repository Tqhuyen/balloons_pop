from src import commons

from src.states.base import State
from src.states.state_menu import MainMenuState

from src.assets.image import AddImage
from src.assets.music import *


class LogoState(State):
    def __init__(self, game):
        super(LogoState, self).__init__(game)

        # Image Logo
        self.img_logo = AddImage("../src/resources/images/Logo.png", self.game.window_rect.center)
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 3000:
            # Activate New State
            new_state = MainMenuState(self.game)
            new_state.enter_state()
            # Music
            load_music("../src/resources/music/relax_music.mp3", commons.music_volume)


    def render(self, window):
        # Background
        window.fill(pygame.Color("black"))
        # Image
        self.img_logo.render(window)