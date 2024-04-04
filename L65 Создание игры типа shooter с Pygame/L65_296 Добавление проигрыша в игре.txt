import pygame
import sys
from random import randint

pygame.init()

game_font = pygame.font.Font(None, 42)

screen_width, screen_height = 800, 600
screen_background = pygame.image.load('images/background.png')
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Shooter")
fighter_image = pygame.image.load('images/fighter2.png')

FIGHTER_STEP = 0.5
fighter_width, fighter_height = fighter_image.get_size()
fighter_x = (screen_width / 2) - (fighter_width / 2)
fighter_y = screen_height - fighter_height
fighter_is_move_left, fighter_is_move_right = False, False

ROCKET_STEP = 0.6
rocket_iamge = pygame.image.load('images/rocket2.png')
rocket_width, rocket_height = rocket_iamge.get_size()
rocket_x = 0
rocket_y = 0
rocket_was_fired = False

ALIEN_STEP = 0.1
alien_iamge = pygame.image.load('images/alien2.png')
alien_width, alien_height = alien_iamge.get_size()
alien_x = randint(0, screen_width - alien_width)  # cordinatele de la inceput
alien_y = 0
alien_was_fired = False

game_is_running = True

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_move_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_move_right = True
            if event.key == pygame.K_SPACE:
                rocket_was_fired = True
                rocket_x = fighter_x + (fighter_width / 2) - (rocket_width / 2)
                rocket_y = fighter_y - rocket_height
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_move_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_move_right = False

    if fighter_is_move_left and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP
    if fighter_is_move_right and fighter_x <= screen_width - fighter_width - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    alien_y += ALIEN_STEP

    if rocket_was_fired and rocket_y + rocket_height < 0:
        rocket_was_fired = False

    if rocket_was_fired:
        rocket_y -= ROCKET_STEP

        # screen.blit(screen_background, (0, 0))
    screen.fill((23, 52, 71))
    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(alien_iamge, (alien_x, alien_y))

    if rocket_was_fired:
        screen.blit(rocket_iamge, (rocket_x, rocket_y))

    pygame.display.update()

    if alien_y + alien_height > fighter_y:
        game_is_running = False

game_over_text = game_font.render("Game Over", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width/2, screen_height/2)
screen.blit(game_over_text, game_over_rectangle)
pygame.display.update()
pygame.time.wait(3000) # 3 secunde asteptam

pygame.quit()