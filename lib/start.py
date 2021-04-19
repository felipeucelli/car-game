def off_screen(sprite):
    return sprite.rect[1] > sprite.rect[3]


def start():
    import pygame
    from .car import Car
    from .collider import Collider
    from .road import Road

    screen_width = 520
    screen_height = 600

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('car-game-in-python')

    car_group = pygame.sprite.Group()
    car = Car()
    car_group.add(car)

    collider_group = pygame.sprite.Group()
    collider = Collider()
    collider_group.add(collider)

    road_group = pygame.sprite.Group()
    for i in range(2):
        road = Road(screen_height * i)
        road_group.add(road)

    for c in range(20):
        collider = Collider()
        collider_group.add(collider)

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

                if event.key == pygame.K_DOWN:
                    car.freeze()

        screen.blit(screen, (0, 0))

        if off_screen(road_group.sprites()[0]):
            road_group.remove(road_group.sprites()[0])

            new_road = Road(screen_height)
            road_group.add(new_road)

        if off_screen(collider_group.sprites()[0]):
            collider_group.remove(collider_group.sprites()[0])

            new_collider = Collider()
            collider_group.add(new_collider)

        road_group.update()
        car_group.update()
        collider_group.update()

        road_group.draw(screen)
        car_group.draw(screen)
        collider_group.draw(screen)

        if pygame.sprite.groupcollide(car_group, collider_group, False, False, collided=pygame.sprite.collide_mask):
            game = False

        pygame.display.update()

    pygame.quit()
