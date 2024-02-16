from pygame import pygame
from button import Button
from play_menu import PlayMenu

pygame.init()
pygame.font.init()

def home_menu(screen):
    play_button = Button('Play', 30, 350, True, screen)
    leader_board_button = Button('Leader Board', 200, 350, True, screen)
    shop_button = Button('Shop', 370, 350, True, screen)
    login_button = Button('Login', 540, 350, True, screen)
    tutorial_button = Button('Tutorial', 710, 350, True, screen)
    setting_button = Button('Settings', 710, 50, True, screen)

    play_button.draw()
    leader_board_button.draw()
    shop_button.draw()
    login_button.draw()
    tutorial_button.draw()
    setting_button.draw()

    if play_button.check_click():
        play_menu = PlayMenu(screen)
        play_menu.display_options()