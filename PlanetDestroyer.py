import pygame

pygame.init()

# Screen and Clock
screen_size = [360, 400]
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# Colors
White = (255, 255, 255)
Black = (0, 0, 0)

# Values
planetList = ["planet1.png", "planet2.png", "planet3.png", "planet4.png"]
planet_index = 0
planet_X = 140
planetAddValue = 5
spaceship_X = 155
bullet_X = 177
bullet_Y = 350
fired = False
score = 0
font = pygame.font.Font('freesansbold.ttf', 28)
keep_alive = True

# Load Images
background = pygame.image.load('bg.jpg')
planet = pygame.image.load(planetList[planet_index])
planet.set_colorkey(Black)
bullet = pygame.image.load('bullet.png')
bullet.set_colorkey(Black)
spaceship = pygame.image.load('spaceship.png')
spaceship.set_colorkey(Black)

# Game Loop
while keep_alive:
    # Keyboard Event
    pygame.event.get()
    keys = pygame.key.get_pressed()

    # Show Background Image, Bullet and Spaceship
    screen.blit(pygame.transform.scale(background, (360, 400)), (0, 0))
    screen.blit(bullet, [bullet_X, bullet_Y])
    screen.blit(spaceship, [spaceship_X, 320])

    # Planet MovingX
    planet_X += planetAddValue
    screen.blit(planet, [planet_X, 50])

    if planet_X == 280:
        planetAddValue = -5
    elif planet_X == 0:
        planetAddValue = 5

    # Bullet and Spaceship Keyboard (MovingX)
    if keys[pygame.K_RIGHT] is True and spaceship_X <= 310:
        bullet_X += 5
        spaceship_X += 5
        screen.blit(bullet, [bullet_X, bullet_Y])
        screen.blit(spaceship, [spaceship_X, 320])
    elif keys[pygame.K_LEFT] is True and spaceship_X >= 0:
        bullet_X -= 5
        spaceship_X -= 5
        screen.blit(bullet, [bullet_X, bullet_Y])
        screen.blit(spaceship, [spaceship_X, 320])

    # Bullet Keyboard (MovingY)
    if keys[pygame.K_SPACE] is True:
        fired = True
    if fired is True:
        bullet_Y -= 5
        if bullet_Y < 75:
            fired = False
            score += 1
            bullet_Y = 350
            # Collision
            if planet_X + 40 > bullet_X > planet_X - 40:
                # Changing Planets
                planet_index += 1
                if planet_index < len(planetList):
                    planet_X = 140
                    planet = pygame.image.load(planetList[planet_index])
                    planet.set_colorkey(Black)
                else:
                    keep_alive = False

    # Quit Game
    if keys[pygame.K_q] is True:
        screen.fill(Black)
        pygame.display.update()
        break

    pygame.display.update()
    clock.tick(60)

# Score Loop
keep_alive2 = True
while keep_alive2:
    # Keyboard Event
    pygame.event.get()
    keys = pygame.key.get_pressed()
    screen.fill(Black)
    text = font.render(f"Total Bullets: {score}", True, White)
    textRect = text.get_rect()
    textRect.center = (360 // 2, 300 // 2)
    screen.blit(text, textRect)

    text2 = font.render("Game Over!", True, White)
    textRect2 = text2.get_rect()
    textRect2.center = (360 // 2, 400 // 2)
    screen.blit(text2, textRect2)
    if keys[pygame.K_q] is True or keys[pygame.K_ESCAPE] is True:
        screen.fill(Black)
        pygame.display.update()
        keep_alive2 = False

    pygame.display.update()
