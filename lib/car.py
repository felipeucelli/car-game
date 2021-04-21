import pygame

screen_width = 520
screen_height = 600


class Car(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.pos_move_x = 0
        self.pos_move_y = 0

        self.image = pygame.image.load('lib/images/car1.png')

        self.rect = self.image.get_rect()
        self.rect[0] = screen_width / 2
        self.rect[1] = screen_height - 100

    def update(self):
        self.rect[0] += self.pos_move_x
        self.rect[1] += self.pos_move_y
        if self.rect[0] <= 10 or self.rect[0] >= 490:
            self.pos_move_x = 0
        if self.rect[1] >= 500 or self.rect[1] <= 100:
            self.pos_move_y = 0

    def move_left(self):
        if self.rect[0] > 10:
            self.pos_move_x = -5

    def move_right(self):
        if self.rect[0] < 490:
            self.pos_move_x = 5

    def move_on(self):
        if self.rect[1] > 100:
            self.pos_move_y = -5

    def move_back(self):
        if self.rect[1] < 500:
            self.pos_move_y = 5

    def freeze(self):
        self.pos_move_x = 0
        self.pos_move_y = 0
