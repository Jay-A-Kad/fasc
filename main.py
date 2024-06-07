import os
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

# setting window
pygame.display.set_caption("The frog ate the space crystal")
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

# display window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# making a player


class Player(pygame.sprite.Sprite):
    COLOR = (0, 255, 0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.direction = 'Left'

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def move_left(self, vel):
        self.x_vel = -vel
        if self.direction != 'left':
            self.direction = 'left'

    def move_right(self, vel):
        self.x_vel = vel
        if self.direction != 'right':
            self.direction = 'right'

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, self.rect)


# handle player movement

def handle_move(player):
    keys = pygame.key.get_pressed()

    player.x_vel = 0
    if keys[pygame.K_LEFT]:
        player.move_left(PLAYER_VEL)
    if keys[pygame.K_RIGHT]:
        player.move_right(PLAYER_VEL)

# prep images for background


def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i*width, j*height)
            tiles.append(pos)

    return tiles, image


# draw the background
def draw(window, background, bg_image, player):
    for tiles in background:
        window.blit(bg_image, tiles)

    player.draw(window)
    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Brown.png")

    player = Player(100, 100, 50, 50)
    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop(FPS)
        handle_move(player)
        draw(window, background, bg_image, player)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
