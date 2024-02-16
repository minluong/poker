#imports
import pygame
from button import Button

class PlayMenu:
    def __init__(self, screen):
        self.screen = screen
        self.new_game_button = Button('New Game', 30, 150, True, self.screen)
        self.load_game_button = Button('Load Game', 200, 150, True, self.screen)

    def display_options(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.screen.fill((0, 50, 32))
            pygame.draw.rect(self.screen, 'light grey', (30, 350, 150, 40))
            pygame.draw.rect(self.screen, 'black', (30, 350, 150, 40), 2)
            play_text = pygame.font.Font("freesansbold.ttf", 18).render("Play", True, 'black')
            self.screen.blit(play_text, (35, 355))

            leaderboard_button = Button('Leaderboard', 200, 350, True, self.screen)
            shop_button = Button('Shop', 370, 350, True, self.screen)
            login_button = Button('Login', 540, 350, True, self.screen)
            tutorial_button = Button('Tutorial', 710, 350, True, self.screen)
            settings_button = Button('Settings', 710, 50, True, self.screen)

            leaderboard_button.draw()
            shop_button.draw()
            login_button.draw()
            tutorial_button.draw()
            settings_button.draw()
            
            self.new_game_button.draw()
            self.load_game_button.draw()

            pygame.display.flip()

            if self.new_game_button.check_click():
                print("New Game Clicked")
                running = False
            elif self.load_game_button.check_click():
                print("Load Game Clicked")
                running = False