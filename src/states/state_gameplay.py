import pygame
import numpy as np
import cv2
import time
from cvzone.HandTrackingModule import HandDetector

from src import commons
from src.states.base import State

from src.assets.text import AddText

class GamePlayState(State):
    def __init__(self, game):
        super(GamePlayState, self).__init__(game)

        # Camera
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, self.game.window_rect.width * 2)
        self.cap.set(4, self.game.window_rect.height * 2)

        # Sound Balloon Pop
        self.sfx_pop = pygame.mixer.Sound("../resources/sounds/pop_balloon.wav")
        self.sfx_pop.set_volume(commons.sfx_volume)

        # Hand Detector
        self.detector = HandDetector(detectionCon=0.8, maxHands=1)

        # Variables
        self.start_time = time.time()
        self.total_time = commons.gameplay_total_time
        commons.score = 0

    def update_cam(self):
        success, self.img = self.cap.read()
        self.img = cv2.flip(self.img, 1)
        self.hands, self.img = self.detector.findHands(self.img, flipType=False)
        self.img_rgb = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.img_rgb = np.rot90(self.img_rgb)
        self.frame = pygame.surfarray.make_surface(self.img_rgb).convert()
        self.frame = pygame.transform.flip(self.frame, True, False)
        self.f_rect = self.frame.get_rect(center=self.game.window_rect.center)

    def update(self, dt):
        pass

    def update_event(self):
        if self.game.pause:
            self.game.pause = False

    def render(self, window):
        self.update_event()
        self.update_cam()
        window.blit(self.frame, self.f_rect)
