import pygame

from dino_runner.utils.constants import BG, ICON, RESET, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
     
        self.score = 0
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.count_death = 0
        
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

    def run(self):
        # Game loop: events - update - draw
        self.reset()
        
        while self.playing:
            self.events()
            self.update()
            self.draw()
        #pygame.quit()

    def execute(self):
        self.executing = True
        
        while(self.executing):
            
            if self.count_death == 0:
                self.display_menu()
            elif self.count_death > 0:
                self.death_menu()
            
        pygame.display.quit()
        pygame.quit()  
            
        pygame.display.quit()
        pygame.quit()
    
    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks())/1000,2)
           
            if time_to_show >=0:
                self.draw_time_to_screen(time_to_show)
                
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
    
    
    def draw_time_to_screen(self, time_to_show):
        
        font_size = 15
        color = (0,0,0)
        FONT = 'freesansbold.ttf'
        font = pygame.font.Font(FONT, font_size)
        
        text_to_display = f"Power up remaining time: {time_to_show}"
               
        text = font.render(text_to_display,True, color)
        text_rect = text.get_rect()
        
        text_rect.x = 70
        text_rect.y = 100
        self.screen.blit(text, (text_rect.x, text_rect.y))
    
    
    def display_menu(self):
        self.screen.fill((255,255,255))
        font_size = 30
        color = (0,0,0)
        font_type = 'freesansbold.ttf'
        font = pygame.font.Font(font_type, font_size)
        text = font.render(f"Press any key to start", True, color)
        score_text_rect = text.get_rect()
        score_text_rect.x = (SCREEN_WIDTH // 2) - (score_text_rect.width // 2)
        score_text_rect.y = (SCREEN_HEIGHT // 2) - (score_text_rect.height // 2)
        self.screen.blit(text, (score_text_rect.x, score_text_rect.y))

        pygame.display.update()
        self.events_on_menu()

    def death_menu(self):
        self.screen.fill((255,255,255))
        font_size = 30
        color = (0,0,0)
        font_type = 'freesansbold.ttf'
        font = pygame.font.Font(font_type, font_size)
        text = font.render(f"Press any key to restart", True, color)
        score = font.render(f"Your Score: " + str(self.score), True, (0,0,0))
        death = font.render(f"Death count: " + str(self.count_death), True, (0,0,0))
        
        scoreRect = score.get_rect()
        scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40)
        self.screen.blit(score, scoreRect)
        
        deathRect = death.get_rect()
        deathRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 75)
        self.screen.blit(death, deathRect)
        
        score_text_rect = text.get_rect()
        score_text_rect.x = (SCREEN_WIDTH // 2) - (score_text_rect.width // 2)
        score_text_rect.y = (SCREEN_HEIGHT // 2) - (score_text_rect.height // 2)
        self.screen.blit(text, (score_text_rect.x, score_text_rect.y))
        
        reset = RESET
        reset_rect = reset.get_rect()
        reset_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 145)
        self.screen.blit(reset, reset_rect)
        
        pygame.display.update()
        self.events_on_menu()   
        
          

        
    def events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.executing = False
            if event.type == pygame.KEYDOWN:
                self.reset()
                self.run()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_game_speed()
        
        self.power_up_manager.update(self)
        
        self.update_score()
        
        

    def update_score(self):
        self.score+= 1
        
    
    def update_game_speed(self):
        if self.score % 100 == 0:           
            self.game_speed+=5
    
    def reset(self):
        self.score = 0
        self.playing = True
        self.game_speed = 20
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_up()
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()

        self.draw_power_up_time()#drawing in the screen
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        
        #draw score
        self.draw_score()

        pygame.display.update()
        pygame.display.flip()

    def draw_score(self):
                
        font_size = 32
        color = (0,0,0)
        FONT = 'freesansbold.ttf'
        
        font = pygame.font.Font(FONT, font_size)
        text = font.render(f"Score: {self.score}", True, color)
        
        score_text_rect =  text.get_rect()
        score_text_rect.x = 850
        score_text_rect.y = 30
        
        self.screen.blit(text, (score_text_rect.x, score_text_rect.y))
        
    
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed