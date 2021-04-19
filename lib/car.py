import pygame

screen_width = 520
screen_height = 600


class Car(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.pos_move = 0

        self.image = pygame.image.load('lib/images/car1.png')

        self.rect = self.image.get_rect()
        self.rect[0] = screen_width / 2
        self.rect[1] = screen_height - 100

    def update(self):
        self.rect[0] += self.pos_move
        if self.rect[0] <= 10 or self.rect[0] >= 490:
            self.pos_move = 0

    def move_left(self):
        if self.rect[0] > 10:
            self.pos_move = -5

    def move_right(self):
        if self.rect[0] < 490:
            self.pos_move = 5

    def freeze(self):
        self.pos_move = 0
