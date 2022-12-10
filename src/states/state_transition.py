from src import commons

from src.states.base import State
from src.states.state_gameplay import GamePlayState

from src.assets.text import AddText
from src.assets.music import *


class TransitionState(State):
    def __init__(self, game):
        super(TransitionState, self).__init__(game)

        # Text Transition
        self.txt_trn = AddText("LOADING...", 'white', 46, self.game.window_rect.center)
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 3000:
            new_state = GamePlayState(self.game)
            new_state.enter_state()
            # Music
            load_music("./src/resources/music/energetic_music.wav", commons.music_volume)

    def render(self, window):
        # Background
        window.fill(pygame.Color('black'))
        # Text
        self.txt_trn.render(window)