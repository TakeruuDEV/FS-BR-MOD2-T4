
import pygame
from dino_runner.components.obstacles.obstacle import Obstacle
from pygame import mixer
from dino_runner.utils.constants import BIRD_SOUND

pygame.init()
Y_POS_BIRD = 250
class Bird(Obstacle):
    def __init__(self, images):
        bird_soundd = mixer.Sound(BIRD_SOUND)
        bird_soundd.play()
        self.type = 0
        super().__init__(images, self.type)
        self.rect.y = Y_POS_BIRD
        self.index = 0

    def draw(self, screen):
        if self.index >= 9:
            self.index = 0
        screen.blit(self.images[self.index//5], self.rect)
        self.index += 1