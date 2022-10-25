
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.LargeCactus import LargeCactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
import pygame
import random

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        
        if len(self.obstacles) == 0:
            if random.randint(0,1) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random.randint(0,1) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))      


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            #manage the collision
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                pygame.time.delay(500)
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
        