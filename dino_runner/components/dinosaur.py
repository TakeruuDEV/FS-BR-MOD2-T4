#Projeto de Fernando Marques dos Santos
#Importando pygame e constants de imagem
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import DUCKING, RUNNING, JUMPING

#Criando constantes globais
X_POS = 80
Y_POS = 310
JUMP_VEL = 8.5
Y_POS_DUCK = 340

class Dinosaur(Sprite):
    def __init__(self):
        #Instacia imagens
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.duck_img = DUCKING

        #Instacia funções
        self.dino_run = True
        self.dino_jump = False 
        self.dino_duck = False       
        
        #Instacia imagens e base para tela
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.jump_vel = JUMP_VEL


    def run(self):
        if self.step_index < 5:
            self.image = RUNNING[0] 
        else:
            self.image = RUNNING[1]
        #Retorna altura base do dino depois do duck
        self.dino_rect.y = Y_POS
             
        self.step_index+=1
        
    def update(self, user_input):
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_duck: #Chama a função duck()
            self.duck()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        # Se o usuário apertar DOWN (Setinha pra baixo) e o dino não estiver pulando na hora:
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True #Self.dino.duck se torna verdadeiro (True)
            self.dino_run = False #Self.dino.run se torna falso (False)
            self.dino_jump = False #Self.dino.jump se torna falso (False)
        # Se o usuário não apertar DOWN (Setinha pra baixo) e o dino não estiver pulando na hora:
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False #Self.dino.duck se torna falso (false)
            self.dino_run = True #Self.dino.run se torna verdadeiro (True)
            self.dino_jump = False #Self.dino.jump se torna falso (falso)

        if self.step_index >=10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    #Função JUMP adicionada
    def jump(self):
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8

        if self.jump_vel < -JUMP_VEL:
            self.dino_rect.y = Y_POS
            self.dino_jump = False
            self.jump_vel = JUMP_VEL

    #Função DUCK adicionada
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1
