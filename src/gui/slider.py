import pygame

class Slider:
    def __init__(self, x, y, width, height, x_scroll, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x_scroll = x_scroll
        self.color = color

    def update(self, window):
        m_pos = pygame.mouse.get_pos()
        m_click = pygame.mouse.get_pressed()

        if self.x + self.width > m_pos[0] > self.x and self.y + self.height + 12 > m_pos[1] > self.y - 12:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))
            if m_click[0] == 1:
                self.x_scroll = m_pos[0]
        else:
            pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))

    def render(self, window):
        self.update(window)
        pygame.draw.rect(window, self.color, [self.x_scroll - 5, self.y - 12, 10, 24])
