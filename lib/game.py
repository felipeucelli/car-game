import pygame
import sys
import os

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

        for c in range(10):
            self.collider = Collider()
            self.collider_group.add(self.collider)

        self.main_loop = True
        self.start_loop = True
        self. game_over_loop = True

        self.score = 0

        self.clock = pygame.time.Clock()

        self.score_font = pygame.font.SysFont('Arial', 30)

    @staticmethod
    def off_screen(sprite):
        return sprite.rect[1] > sprite.rect[3]

    def start_game(self):
        level = 30
        pseudo_level = 0
        while self.main_loop:
            self.clock.tick(level)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.main_loop = False
                    self.start_loop = False
                    self.game_over_loop = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.main_loop = False
                        self.start_loop = False
                        self.game_over_loop = False
                        break
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
                self.score += 1
                if self.score <= 300:
                    pseudo_level += 1

            self.road_group.update()
            self.car_group.update()
            self.collider_group.update()

            self.road_group.draw(self.screen)
            self.car_group.draw(self.screen)
            self.collider_group.draw(self.screen)

            if pygame.sprite.groupcollide(self.car_group, self.collider_group, False, False,
                                          collided=pygame.sprite.collide_mask):
                self.game_over()

            score_text = self.score_font.render('SCORE: ' + str(self.score), True, (0, 0, 0))
            self.screen.blit(score_text, (10, 5))

            if pseudo_level == 50 and self.score <= 300:
                level += 5
                pseudo_level = 0

            pygame.display.update()

    def start(self):
        font = pygame.font.SysFont('Arial', 40)
        text = font.render('Press SPACE to start', True, (225, 225, 255))
        self.screen.blit(text, (70, 200))
        pygame.display.update()
        while self.start_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.start_loop = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.start_loop = False
                        break
                    if event.key == pygame.K_SPACE:
                        self.main_loop = True
                        self.start_game()

    def game_over(self):
        font = pygame.font.SysFont('Arial', 40)
        text_1 = font.render('Gamer Over', True, (255, 0, 0))
        text_2 = font.render('Press SPACE to start again', True, (0, 0, 0))
        self.screen.blit(text_1, (150, 200))
        self.screen.blit(text_2, (20, 300))

        score_text = self.score_font.render('SCORE: ' + str(self.score), True, (0, 0, 0))
        self.screen.blit(score_text, (10, 5))

        pygame.display.update()
        while self.game_over_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.start_loop = False
                    self.main_loop = False
                    self.game_over_loop = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.start_loop = False
                        self.main_loop = False
                        self.game_over_loop = False
                        break
                    if event.key == pygame.K_SPACE:
                        self.restart()

        pygame.display.update()

    @staticmethod
    def restart():
        python = sys.executable
        os.execl(python, python, * sys.argv)

    pygame.quit()
