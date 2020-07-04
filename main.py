import pygame

screen = pygame.display.set_mode((1200, 1000))
pygame.init()


class Menu:
    def __init__(self):
        self.background = pygame.image.load("resources/images/main_background.jpg")
        pygame.font.init()
        myfont = pygame.font.SysFont('Arial', 50)
        self.textsurface = myfont.render('Ubongo', False, (0, 0, 0))
        self.arrow = pygame.image.load("resources/images/arrow.png")
        self.x = 450
        self.y = 560
        self.election = 1

    def dibujar(self):
        screen.blit(self.background, (0, 0))
        screen.blit(self.arrow, (self.x, self.y))
        # screen.blit(self.textsurface,(500,200))

    def mover(self, dir):

        if dir == 'up' and 1 < self.election:
            self.y -= 100
            self.election -= 1
        if dir == 'down' and self.election < 4:
            self.y += 100
            self.election += 1

    def select(self):
        if self.election == 4:
            global running
            running = False


menu = Menu()

running = True
while running:
    screen.fill((255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_DOWN:
                menu.mover('down')
            elif event.key == pygame.K_UP:
                menu.mover('up')
            elif event.key == pygame.K_RETURN:
                menu.select()
    menu.dibujar()
    pygame.display.update()


