import pygame
from src import commons

from src.gui.button import Button
from src.gui.slider import Slider

from src.assets.text import AddText
from src.assets.image import AddImage

from src.states.base import State

class OptionsState(State):
    def __init__(self, game):
        super(OptionsState, self).__init__(game)

        # Image Background
        self.img_background = AddImage("../src/resources/images/Sky.png", self.game.window_rect.center)

        # Text Title
        self.txt_ttl_top = AddText("OPTIONS", 'white', 46,
                                    (self.game.window_rect.centerx, self.game.window_rect.centery - 270))
        self.txt_ttl_bot = AddText("OPTIONS", 'gray', 46,
                                    (self.game.window_rect.centerx, self.game.window_rect.centery - 264))

        # Text Music Volume
        self.txt_m_volume_top = AddText("MUSIC:", 'white', 36,
                                   (self.game.window_rect.centerx - 130, self.game.window_rect.centery - 50))
        self.txt_m_volume_bot = AddText("MUSIC:", 'gray', 36,
                                    (self.game.window_rect.centerx - 130, self.game.window_rect.centery - 44))

        # Text SFX Volume
        self.txt_sfx_volume_top = AddText("SFX:", 'white', 36,
                                        (self.game.window_rect.centerx - 130, self.game.window_rect.centery + 50))
        self.txt_sfx_volume_bot = AddText("SFX:", 'gray', 36,
                                        (self.game.window_rect.centerx - 130, self.game.window_rect.centery + 56))

        # Buttons
        self.btn_return = Button("RETURN", 200, 40,
                                 (self.game.window_rect.centerx - 70, self.game.window_rect.centery + 250), 6)

        # Sliders
        self.current_music_volume = 150*commons.music_volume + 500
        self.current_sfx_volume = 150*commons.sfx_volume + 500
        self.sld_m_vol = Slider(500, 310, 150, 2, self.current_music_volume, 'white')
        self.sld_sfx_vol = Slider(500, 410, 150, 2, self.current_sfx_volume, 'white')

    def update(self, dt):
        if self.btn_return.pressed:
            self.exit_state()
            self.btn_return.pressed = False

    def render(self, window):
        # Background
        self.img_background.render(window)
        # Text
        self.txt_ttl_bot.render(window)
        self.txt_ttl_top.render(window)
        self.txt_m_volume_bot.render(window)
        self.txt_m_volume_top.render(window)
        self.txt_sfx_volume_bot.render(window)
        self.txt_sfx_volume_top.render(window)
        # Slider
        self.sld_m_vol.render(window)
        self.sld_sfx_vol.render(window)
        # Button
        self.btn_return.render(window)

        # Logic
        commons.music_volume = (1.0 / 150) * (self.sld_m_vol.x_scroll - 500)
        commons.sfx_volume = (1.0 / 150) * (self.sld_sfx_vol.x_scroll - 500)
        pygame.mixer.music.set_volume(commons.music_volume)

