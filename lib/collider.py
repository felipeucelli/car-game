import pygame
from random import randint, randrange


class Collider(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        if randint(0, 9) % 2 == 0:
            self.image = pygame.image.load('lib/images/car2.png')
        else:
            self.image = pygame.image.load('lib/images/car3.png')

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        self.rect[1] = randrange(-1000, 0, 80)
        self.rect[0] = randrange(20, 490, 40)
        self.rect[3] = 600

    def update(self):
        self.rect[1] += 12
