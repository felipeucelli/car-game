import pygame

screen_width = 520
screen_height = 600

ground_height = screen_height
ground_width = 100


class Car(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.pos_move = 0

        self.image = pygame.image.load('images/car1.png')

        self.rect = self.image.get_rect()
        self.rect[0] = screen_width / 2
        self.rect[1] = screen_height - 100

    def update(self):
        self.rect[0] += self.pos_move

    def move_left(self):
        self.pos_move = -5

    def move_right(self):
        self.pos_move = 5

    def freeze(self):
        self.pos_move = 0


class Road(pygame.sprite.Sprite):

    def __init__(self, y_pos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('images/road.png')
        self.image = pygame.transform.scale(self.image, (screen_width, ground_height))
        self.rect = self.image.get_rect()
        self.rect[1] = -y_pos

    def update(self):
        self.rect[1] += 10


def off_screen(sprite):
    return sprite.rect[1] > sprite.rect[3]


pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('car-game-in-python')

car_group = pygame.sprite.Group()
car = Car()
car_group.add(car)

road_group = pygame.sprite.Group()
for i in range(2):
    road = Road(screen_height * i)
    road_group.add(road)

clock = pygame.time.Clock()

game = True
while game:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False

            if event.key == pygame.K_LEFT:
                car.move_left()

            if event.key == pygame.K_RIGHT:
                car.move_right()

            if event.key == pygame.K_SPACE:
                car.freeze()

    screen.blit(screen, (0, 0))

    if off_screen(road_group.sprites()[0]):
        road_group.remove(road_group.sprites()[0])

        new_road = Road(screen_height)
        road_group.add(new_road)

    road_group.update()
    car_group.update()

    road_group.draw(screen)
    car_group.draw(screen)

    pygame.display.update()

pygame.quit()
