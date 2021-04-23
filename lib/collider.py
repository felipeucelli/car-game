# -*- coding: utf-8 -*-

# @autor: Felipe Ucelli
# @github: github.com/felipeucelli

# Built-ins
import pygame
from random import randint, randrange


class Collider(pygame.sprite.Sprite):
    """
    Classe responsável pela criação e configuração dos carros
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Carrega um carro aleatório
        if randint(0, 9) % 2 == 0:
            self.image = pygame.image.load('lib/images/car2.png')
        else:
            self.image = pygame.image.load('lib/images/car3.png')

        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect()
        # Gera um carro em uma posição aleatória
        self.rect[1] = randrange(-1000, 0, 80)
        self.rect[0] = randrange(20, 490, 40)
        self.rect[3] = 600

    def update(self):
        """
        Responsável por atualiza a posição do carro
        :return:
        """
        self.rect[1] += 12
