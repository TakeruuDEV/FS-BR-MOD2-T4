import random
from dino_runner.components.dinosaur import Y_POS_DUCK
from dino_runner.components.obstacles.obstacle import Obstacle

Y_POS_CACTUS = 325
class Cactus(Obstacle):
    def __init__(self, images):
        self.type = random.randint(0,2)
        super().__init__(images, self.type)

        self.rect.y = Y_POS_CACTUS