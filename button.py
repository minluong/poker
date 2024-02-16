#imports
import pygame
pygame.init()
pygame.font.init()

font = pygame.font.Font("freesansbold.ttf", 18)

#creating buttons
class Button:
    def __init__(self, text, x_pos, y_pos, enabled, screen):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.screen = screen
    
    def draw(self):
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.Rect(self.x_pos, self.y_pos, 150, 40)
        pygame.draw.rect(self.screen, 'light grey' if self.enabled else 'black', button_rect)
        pygame.draw.rect(self.screen, 'black', button_rect, 2)
        self.screen.blit(button_text, (self.x_pos + 5, self.y_pos + 5))

    def check_click(self):
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.Rect(self.x_pos, self.y_pos, 150, 40)

        return self.enabled and left_click and button_rect.collidepoint(pygame.mouse.get_pos())