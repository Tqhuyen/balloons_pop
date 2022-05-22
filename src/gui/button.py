import pygame
from src.assets.text import AddText

class Button:
    def __init__(self, text, width, height, pos, elevation):
        self.pressed = False
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

        # Top rectangle
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # Bottom rectangle
        self.bottom_rect = pygame.Rect(pos, (width, height))
        self.bottom_color = '#354B5E'

        # Text
        self.text = AddText(text, '../resources/fonts/SweetUnicorn.ttf', 'white', 20, self.top_rect.center)

        # Sound
        self.btn_click = pygame.mixer.Sound("../resources/sounds/button_click.wav")

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed:
                    self.btn_click.play()
                    self.pressed = False

        else:
            self.dynamic_elevation = self.elevation
            self.top_color = '#475F77'

    def anim_button(self):
        # Elevation Logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text.text_rect.center = self.top_rect.center
        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

    def render(self, window):
        self.anim_button()
        pygame.draw.rect(window, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(window, self.top_color, self.top_rect, border_radius=12)
        self.text.render(window)
        self.check_click()