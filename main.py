import pygame
import Tablero
import Controller

screen = pygame.display.set_mode((1200, 1000))
pygame.init()


class Menu:
    def __init__(self):
        self.background = pygame.image.load("resources/images/main_background.jpg")
        self.background_1 = pygame.image.load("resources/images/table.jpg")
        self.tablero_img = pygame.image.load("resources/images/tablero.png")
        self.plantilla_img = pygame.image.load("resources/images/plantilla.png")
        pygame.font.init()
        myfont = pygame.font.SysFont('Arial', 50)
        self.textsurface = myfont.render('Ubongo', False, (0, 0, 0))
        self.arrow = pygame.image.load("resources/images/arrow.png")
        self.x = 450
        self.y = 560
        self.election = 1
        self.Fase_Menu = True
        self.Fase_Tablero_ini = False
        self.Fase_Puzzle = False
        self.Fase_Tablero = False
        self.Tablero_Ubongo = Tablero.Tablero()
        self.gema_roja = pygame.image.load("resources/images/gema_roja.png")
        self.gema_azul = pygame.image.load("resources/images/gema_azul.png")
        self.gema_verde = pygame.image.load("resources/images/gema_verde.png")
        self.gema_morada = pygame.image.load("resources/images/gema_morado.png")
        self.controlador = Controller.Controller()
        self.pc_img = pygame.image.load("resources/images/Pc.png")
        self.jugador_img = pygame.image.load("resources/images/Jugador.png")

        self.posComputadora = 0

    def dibujar(self):
        if self.Fase_Menu:
            screen.blit(self.background, (0, 0))
            screen.blit(self.arrow, (self.x, self.y))
        if self.Fase_Puzzle:
            screen.blit(self.background_1, (0, 0))
            screen.blit(self.plantilla_img,(100,100))
            # screen.blit(self.arrow, (self.x, self.y))
        if self.Fase_Tablero:
            screen.blit(self.background_1, (0, 0))
            screen.blit(self.tablero_img, (100, 0))
            posY = 75
            for x in self.Tablero_Ubongo.tablero:
                posX = 450
                for y in x:
                    if y == 1:
                        screen.blit(self.gema_azul, (posX, posY), )
                    if y == 2:
                        screen.blit(self.gema_morada, (posX, posY))
                    if y == 3:
                        screen.blit(self.gema_roja, (posX, posY))
                    if y == 4:
                        screen.blit(self.gema_verde, (posX, posY))
                    posX += 110
                posY += 65
            # screen.blit(self.arrow, (self.x, self.y))

            screen.blit(self.pc_img, (250, 80 + self.controlador.Jugadores[1].posY * 60))
            screen.blit(self.jugador_img, (200, 80 + self.controlador.Jugadores[0].posY * 60))
            # screen.blit(self.arrow, (self.x, self.y))
        if self.Fase_Tablero_ini:
            screen.blit(self.background_1, (0, 0))
            screen.blit(self.tablero_img, (100, 0))
            posY = 75
            for x in self.Tablero_Ubongo.tablero:
                posX = 450
                for y in x:
                    if y == 1:
                        screen.blit(self.gema_azul, (posX, posY), )
                    if y == 2:
                        screen.blit(self.gema_morada, (posX, posY))
                    if y == 3:
                        screen.blit(self.gema_roja, (posX, posY))
                    if y == 4:
                        screen.blit(self.gema_verde, (posX, posY))
                    posX += 110
                posY += 65
            # screen.blit(self.arrow, (self.x, self.y))

            screen.blit(self.pc_img, ( 250,80 +self.controlador.Jugadores[1].posY * 60))
            screen.blit(self.jugador_img, ( 200,80+self.controlador.Jugadores[0].posY *60))

        # screen.blit(self.textsurface,(500,200))
    def moverFicha(self,dir):
        self.controlador.mover(dir)


    def cambiarfase(self):
        if self.Fase_Menu:
            self.Fase_Menu = False
            self.Fase_Tablero_ini = True
        elif self.Fase_Puzzle:
            self.Fase_Puzzle = False
            self.Fase_Tablero = True
        elif self.Fase_Tablero:
            self.Fase_Tablero = False
            self.Fase_Puzzle = True
        elif self.Fase_Tablero_ini:
            self.Fase_Tablero_ini = False
            self.Fase_Puzzle = True

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
                menu.moverFicha('abajo')
            elif event.key == pygame.K_UP:
                menu.mover('up')
                menu.moverFicha('arriba')
            elif event.key == pygame.K_RETURN:
                menu.cambiarfase()
    menu.dibujar()
    pygame.display.update()
