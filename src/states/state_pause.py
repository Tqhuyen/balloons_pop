from src import commons

from src.states.base import State
from src.assets.text import AddText
from src.assets.music import *
from src.gui.button import Button

class PauseState(State):
    def __init__(self, game):
        super(PauseState, self).__init__(game)

        # Texts
        self.txt_ttl_top = AddText("PAUSE", "white", 56,
                                (self.game.window_rect.centerx, self.game.window_rect.centery - 200))
        self.txt_ttl_bot = AddText("PAUSE", "gray", 56,
                                (self.game.window_rect.centerx, self.game.window_rect.centery - 195))

        # Buttons
        self.btn_resume = Button("RESUME", 200, 40,
                                (self.game.window_rect.x + 200, self.game.window_rect.centery + 120), 6)
        self.btn_menu = Button("MENU", 200, 40,
                                 (self.game.window_rect.centerx + 160, self.game.window_rect.centery + 120), 6)

    def update(self, dt):
        if self.btn_resume.pressed or self.game.pause:
            self.exit_state()
            commons.time_remain += 20
            self.btn_resume.pressed = False
            self.game.pause = False

        if self.btn_menu.pressed:
            while len(self.game.state_stack) > 2:
                self.game.state_stack.pop()
                load_music("../resources/music/relax_music.mp3", commons.music_volume)
                self.btn_menu.pressed = False

    def render(self, window):
        self.txt_ttl_bot.render(window)
        self.txt_ttl_top.render(window)
        self.btn_resume.render(window)
        self.btn_menu.render(window)


