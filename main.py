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


# flip a sprite
def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]


def load_sprite_sheets(dir1, dir2, width, height, direction=True):
    path = join("assets", dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}
    for image in images:
        sprite_sheets = pygame.image.load(join(path, image)).convert_alpha()

        sprites = []
        for i in range(sprite_sheets.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width,  height)
            surface.blit(sprite_sheets, (0, 0), rect)
            sprites.append(pygame.transform.scale2x(surface))

        if direction:
            all_sprites[image.replace(".png", "") + "_right"] = sprites
            all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
        else:
            all_sprites[image.replace(".png", "") + "_right"] = sprites

    return all_sprites
    # making a player


class Player(pygame.sprite.Sprite):
    COLOR = (0, 255, 0)
    SPRITES = load_sprite_sheets("MainCharacters", "NinjaFrog", 32, 32, True)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.direction = 'left'

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
        self.sprite = self.SPRITES["idle_" + self.direction][0]
        win.blit(self.sprite, (self.rect.x, self.rect.y))


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
