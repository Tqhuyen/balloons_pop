from src import commons
from src.states.base import State

from src.assets.image import AddImage
from src.assets.text import AddText
from src.gui.button import Button

class GameOverState(State):
    def __init__(self, game):
        super(GameOverState, self).__init__(game)
        self.high_score = ''
        # Background Image
        self.img_background = AddImage("../resources/images/Sky.png", self.game.window_rect.center)

        # Texts
        self.txt_ttl_top = AddText("TIME IS UP", "white", 56,
                                        (self.game.window_rect.centerx, self.game.window_rect.centery - 200))
        self.txt_ttl_bot = AddText("TIME IS UP", "gray", 56,
                                        (self.game.window_rect.centerx, self.game.window_rect.centery - 195))

        self.txt_score_top = AddText(f"YOUR SCORE: {commons.score}", "white", 30,
                                        (self.game.window_rect.centerx, self.game.window_rect.centery + 25))
        self.txt_score_bot = AddText(f"YOUR SCORE: {commons.score}", "gray", 30,
                                        (self.game.window_rect.centerx, self.game.window_rect.centery + 30))

        # Buttons
        self.btn_restart = Button("RESTART", 200, 40,
                                  (self.game.window_rect.x + 200, self.game.window_rect.centery + 120), 6)
        self.btn_menu = Button("MENU", 200, 40,
                                  (self.game.window_rect.centerx + 160, self.game.window_rect.centery + 120), 6)

    def update(self, dt):
        if self.btn_restart.pressed:
            while len(self.game.state_stack) > 3:
                self.game.state_stack.pop()
                self.btn_restart.pressed = False

        if self.btn_menu.pressed:
            while len(self.game.state_stack) > 2:
                self.game.state_stack.pop()
                self.btn_menu.pressed = False

    def update_score(self):
        with open("../resources/txt/high_score.txt", "r+") as f:
            self.high_score = f.readline()
            f.seek(0)
            if self.high_score < str(commons.score):
                f.write(str(commons.score))
                f.truncate()
            f.close()
        self.txt_high_score_top = AddText(f"HIGH SCORE: {self.high_score}", "white", 30,
                                          (self.game.window_rect.centerx, self.game.window_rect.centery - 60))
        self.txt_high_score_bot = AddText(f"HIGH SCORE: {self.high_score}", "gray", 30,
                                          (self.game.window_rect.centerx, self.game.window_rect.centery - 55))

    def render(self, window):
        self.update_score()
        self.img_background.render(window)
        self.txt_ttl_bot.render(window)
        self.txt_ttl_top.render(window)
        self.txt_high_score_bot.render(window)
        self.txt_high_score_top.render(window)
        self.txt_score_bot.render(window)
        self.txt_score_top.render(window)
        self.btn_restart.render(window)
        self.btn_menu.render(window)
