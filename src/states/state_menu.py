from src.states.base import State
from src.states.state_options import OptionsState
from src.states.state_transition import TransitionState

from src.gui.button import Button
from src.assets.text import AddText
from src.assets.image import AddImage

class MainMenuState(State):
    def __init__(self, game):
        super(MainMenuState, self).__init__(game)

        # Images Background
        self.img_background = AddImage("../src/resources/images/Sky.png", self.game.window_rect.center)
        self.img_balloons = AddImage("../src/resources/images/Balloons.png", self.game.window_rect.center)

        # Text Title
        self.txt_ttl_top = AddText("BALLOON POP", "white", 84,
                            (self.game.window_rect.centerx, self.game.window_rect.centery - 100))
        self.txt_ttl_bot = AddText("BALLOON POP", "gray", 84,
                            (self.game.window_rect.centerx, self.game.window_rect.centery - 94))

        # Buttons
        self.btn_start = Button("START", 200, 40,
                            (self.game.window_rect.centerx - 70, self.game.window_rect.centery + 50), 6)
        self.btn_options = Button("OPTIONS", 200, 40,
                            (self.game.window_rect.centerx - 70, self.game.window_rect.centery + 110), 6)
        self.btn_quit = Button("QUIT", 200, 40,
                            (self.game.window_rect.centerx - 70, self.game.window_rect.centery + 170), 6)

    def update(self, dt):
        if self.btn_start.pressed:
            new_state = TransitionState(self.game)
            new_state.enter_state()
            self.btn_start.pressed = False

        if self.btn_options.pressed:
            new_state = OptionsState(self.game)
            new_state.enter_state()
            self.btn_options.pressed = False

        if self.btn_quit.pressed:
            self.game.playing = False
            self.game.running = False

    def render(self, window):
        # Background
        self.img_background.render(window)
        self.img_balloons.render(window)
        # Texts
        self.txt_ttl_bot.render(window)
        self.txt_ttl_top.render(window)
        # Buttons
        self.btn_start.render(window)
        self.btn_options.render(window)
        self.btn_quit.render(window)
