import pygame
from .car import Car
from .collider import Collider
from .road import Road


class Game:
    def __init__(self):
        pygame.init()

        self.screen_width = 520
        self.screen_height = 600

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('car-game-in-python')

        self.car_group = pygame.sprite.Group()
        self.car = Car()

        self.collider_group = pygame.sprite.Group()
        self.collider = Collider()

        self.car_group.add(self.car)

        self.collider_group.add(self.collider)

        self.road_group = pygame.sprite.Group()
        for i in range(2):
            self.road = Road(self.screen_height * i)
            self.road_group.add(self.road)

        for c in range(20):
            self.collider = Collider()
            self.collider_group.add(self.collider)

        self.main_loop = True

        self.clock = pygame.time.Clock()

    @staticmethod
    def off_screen(sprite):
        return sprite.rect[1] > sprite.rect[3]

    def start(self):
        while self.main_loop:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.main_loop = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_loop = False
                    if event.key == pygame.K_LEFT:
                        self.car.move_left()
                    if event.key == pygame.K_RIGHT:
                        self.car.move_right()
                    if event.key == pygame.K_DOWN:
                        self.car.move_back()
                    if event.key == pygame.K_UP:
                        self.car.move_on()
                if event.type == pygame.KEYUP:
                    self.car.freeze()

            self.screen.blit(self.screen, (0, 0))

            if self.off_screen(self.road_group.sprites()[0]):
                self.road_group.remove(self.road_group.sprites()[0])

                new_road = Road(self.screen_height)
                self.road_group.add(new_road)

            if self.off_screen(self.collider_group.sprites()[0]):
                self.collider_group.remove(self.collider_group.sprites()[0])

                new_collider = Collider()
                self.collider_group.add(new_collider)

            self.road_group.update()
            self.car_group.update()
            self.collider_group.update()

            self.road_group.draw(self.screen)
            self.car_group.draw(self.screen)
            self.collider_group.draw(self.screen)

            if pygame.sprite.groupcollide(self.car_group, self.collider_group, False, False,
                                          collided=pygame.sprite.collide_mask):
                self.main_loop = False

            pygame.display.update()

    pygame.quit()
