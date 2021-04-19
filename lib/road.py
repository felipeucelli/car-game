import pygame

screen_width = 520
screen_height = 600


class Road(pygame.sprite.Sprite):

    def __init__(self, y_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('lib/images/road.png')
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[1] = -y_pos

    def update(self):
        self.rect[1] += 10
