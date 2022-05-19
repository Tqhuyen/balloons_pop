import pygame
import commons

class Game():
    def __init__(self, window):
        self.running, self.playing, self.pause = True, True, False
        self.window = window
        self.window_rect = self.window.get_rect()
        self.clock = pygame.time.Clock()
        self.fps = commons.fps
        self.state_stack = []
        self.load_states()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.pause = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.pause = False

    def load_states(self):
        pass

    def update(self, dt):
        self.state_stack[-1].update(dt)

    def render(self):
        self.state_stack[-1].render(self.window)

    def run(self):
        while self.playing:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.render()
            pygame.display.update()

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((commons.screen_w, commons.screen_h))
    pygame.display.set_caption("Balloon Pop")
    game = Game(window)
    while game.running:
        game.run()
