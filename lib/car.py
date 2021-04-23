# -*- coding: utf-8 -*-

# @autor: Felipe Ucelli
# @github: github.com/felipeucelli

# Built-in
import pygame

# Seta as propriedades da tela
screen_width = 520
screen_height = 600


class Car(pygame.sprite.Sprite):
    """
    Classe responsável pela criação, configuração e interação do player
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Seta a posição de movimento inicial do player
        self.pos_move_x = 0
        self.pos_move_y = 0

        # Carrega a imagem do player
        self.image = pygame.image.load('lib/images/car1.png')

        self.rect = self.image.get_rect()
        # Seta a posição inicial do player
        self.rect[0] = screen_width / 2
        self.rect[1] = screen_height - 100

    def update(self):
        """
        Responsável por atualizar o estado e a posição do player
        :return:
        """
        self.rect[0] += self.pos_move_x
        self.rect[1] += self.pos_move_y
        if self.rect[0] <= 10 or self.rect[0] >= 490:
            self.pos_move_x = 0
        if self.rect[1] >= 500 or self.rect[1] <= 100:
            self.pos_move_y = 0

    def move_left(self):
        """
        Move o player para esquerda
        :return:
        """
        if self.rect[0] > 10:
            self.pos_move_x = -5

    def move_right(self):
        """
        Move o player para a direita
        :return:
        """
        if self.rect[0] < 490:
            self.pos_move_x = 5

    def move_on(self):
        """
        Move o player para frente
        :return:
        """
        if self.rect[1] > 100:
            self.pos_move_y = -5

    def move_back(self):
        """
        Move o player para trás
        :return:
        """
        if self.rect[1] < 500:
            self.pos_move_y = 5

    def freeze(self):
        """
        Faz o carro parar de se mover
        :return:
        """
        self.pos_move_x = 0
        self.pos_move_y = 0
