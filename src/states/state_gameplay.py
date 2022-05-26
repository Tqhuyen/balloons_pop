import pygame
import numpy as np
import cv2
import time
from cvzone.HandTrackingModule import HandDetector

from src import commons
from src.states.base import State
from src.states.state_gameover import GameOverState
from src.enemies.balloon import Balloon

from src.assets.text import AddText

class GamePlayState(State):
    def __init__(self, game):
        super(GamePlayState, self).__init__(game)

        # Camera
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.game.window_rect.width * 2)
        self.cap.set(4, self.game.window_rect.height * 2)

        # Balloons
        self.bal_red = Balloon(game, "../resources/images/Balloons-Red.png", 412, commons.speed_balloon)
        self.bal_black = Balloon(game, "../resources/images/Balloons-Black.png", 624, commons.speed_balloon)
        self.bal_green = Balloon(game, "../resources/images/Balloons_Green.png", 212, commons.speed_balloon)
        self.bal_green_bl = Balloon(game, "../resources/images/Balloons_GreenBlue.png", 824, commons.speed_balloon)

        # Sound Balloon Pop
        self.sfx_pop = pygame.mixer.Sound("../resources/sounds/pop_balloon.wav")
        self.sfx_pop.set_volume(commons.sfx_volume)

        # Hand Detector
        self.detector = HandDetector(detectionCon=0.8, maxHands=1)

        # Variables
        self.start_time = time.time()
        self.total_time = commons.gameplay_total_time
        commons.score = 0

    def update_balloon(self, window):
        if self.hands:
            hand = self.hands[0]
            x, y = hand['lmList'][8]
            if self.bal_red.image.rect.collidepoint(x, y):
                commons.score += commons.score_red
                self.sfx_pop.play()
                point_red = AddText(f"+{commons.score_red}", 'blue', 40,
                                    (self.bal_red.image.rect.x, self.bal_red.image.rect.y))
                point_red.render(window)
                self.bal_red.reset_balloon()

            if self.bal_black.image.rect.collidepoint(x, y):
                commons.score -= commons.score_black
                self.sfx_pop.play()
                point_black = AddText(f"-{commons.score_black}", 'red', 40,
                                    (self.bal_black.image.rect.x, self.bal_black.image.rect.y))
                point_black.render(window)
                self.bal_black.reset_balloon()

            if self.bal_green.image.rect.collidepoint(x, y):
                commons.score += commons.score_green
                self.sfx_pop.play()
                point_green = AddText(f"+{commons.score_green}", 'blue', 40,
                                    (self.bal_green.image.rect.x, self.bal_green.image.rect.y))
                point_green.render(window)
                self.bal_green.reset_balloon()

            if self.bal_green_bl.image.rect.collidepoint(x, y):
                commons.score += commons.score_green_bl
                self.sfx_pop.play()
                point_green_bl = AddText(f"+{commons.score_green_bl}", 'blue', 40,
                                    (self.bal_green_bl.image.rect.x, self.bal_green_bl.image.rect.y))
                point_green_bl.render(window)
                self.bal_green_bl.reset_balloon()

    def update_cam(self, window):
        success, self.img = self.cap.read()
        self.img = cv2.flip(self.img, 1)
        self.hands, self.img = self.detector.findHands(self.img, flipType=False)
        self.img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.img_rgb = np.rot90(self.img_rgb)
        self.frame = pygame.surfarray.make_surface(self.img_rgb).convert()
        self.frame = pygame.transform.flip(self.frame, True, False)
        self.f_rect = self.frame.get_rect(center=self.game.window_rect.center)
        window.blit(self.frame, self.f_rect)

    def update(self, dt):
        pass

    def update_event(self):
        if self.game.pause:
            self.game.pause = False

    def render(self, window):
        commons.time_remain = int(self.total_time - (time.time() - self.start_time))
        if commons.time_remain <= 0:
            new_state = GameOverState(self.game)
            new_state.enter_state()
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            pygame.mixer.music.load("../resources/music/relax_music.mp3")
            pygame.mixer.music.set_volume(commons.music_volume)
            pygame.mixer.music.play(-1)
        else:
            # Updates
            self.update_event()
            self.update_cam(window)
            self.update_balloon(window)

            # Texts
            text_score = AddText(f"SCORE: {commons.score}", 'white', 22, (80, 15))
            text_score.render(window)
            text_time = AddText(f"TIME: {commons.time_remain}", 'white', 22,
                                (self.game.window_rect.width - 100, 15))
            text_time.render(window)
            # Balloons
            self.bal_red.render(window)
            self.bal_black.render(window)
            self.bal_green.render(window)
            self.bal_green_bl.render(window)

