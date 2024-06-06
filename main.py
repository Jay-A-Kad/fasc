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

# display window
window = pygame.display.set_mode((WIDTH, HEIGHT))


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
def draw(window, background, bg_image):
    for tiles in background:
        window.blit(bg_image, tiles)
    pygame.display.update()


def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Brown.png")

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window, background, bg_image)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
