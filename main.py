import pygame
from button import Button
from play_menu import PlayMenu

pygame.init()
pygame.font.init()

WIDTH = 900
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])
fps = 20
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 40)
pygame.display.set_caption('POkeR')

DARK_GREEN = (1, 50, 32)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

run = True
play_button = Button('Play', 30, 350, True, screen)
leaderboard_button = Button('Leaderboard', 200, 350, True, screen)
shop_button = Button('Shop', 370, 350, True, screen)
login_button = Button('Login', 540, 350, True, screen)
tutorial_button = Button('Tutorial', 710, 350, True, screen)
settings_button = Button('Settings', 710, 50, True, screen)

while run:
    screen.fill(DARK_GREEN)
    timer.tick(fps)

    draw_text("poker", font, 'black', 400, 150)

    play_button.draw()
    leaderboard_button.draw()
    shop_button.draw()
    login_button.draw()
    tutorial_button.draw()
    settings_button.draw()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Handle button clicks
    if play_button.check_click():
        play_menu = PlayMenu(screen)
        play_menu.display_options()

    pygame.display.flip()

pygame.quit()