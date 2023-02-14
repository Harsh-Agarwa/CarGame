import pygame
import time
import math

from utils import scale_image, blit_rotate_center

GRASS = scale_image(pygame.image.load("grass.jpg"), 50)
TRACKY = scale_image(pygame.image.load("tracky.png"), 0.9)

TRACK_BORDER = scale_image(pygame.image.load("track2.png"), 0.9)
FINISH = scale_image(pygame.image.load("finish.png"), 0.08)

car8 = scale_image(pygame.image.load("car8.png"), 0.1)
car2 = scale_image(pygame.image.load("car2.png"), 0.55)
WIDTH, HEIGHT = TRACKY.get_width(), TRACKY.get_height()
WIN = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption(" CAR RACING GAME")

FPS = 60
class AbstractCar:
    
    def __init__(self, max_vel, rotation_vel):
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = 0
        self.x, self.y = self.START_POS
        self.accelaration = 0.1




    def rotate(self , left=False, right= False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img , (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel= min(self.vel + self.accelaration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizantal = math.sin(radians) * self.vel

        self.y -=vertical
        self.x -=horizantal

    def reduce_speed(self):
        self.vel = max(self.vel - self.accelaration / 2, 0)
        self.move()


class PlayerCar(AbstractCar):
    IMG = car8
    START_POS = (102,100)



def draw(win, images, player_car):
    for img, pos in images:
        win.blit(img, pos)

    player_car.draw(win)
    pygame.display.update()
run = True
clock = pygame.time.Clock()
images =[(GRASS, (100,100)) , (TRACKY, (0,0)), (FINISH, (125,110))]

player_car = PlayerCar(4,4)




while run:
    clock.tick(FPS)
    draw(WIN, images, player_car)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved= True
        player_car.move_forward()

    if not moved:
        player_car.reduce_speed()

pygame.quit()