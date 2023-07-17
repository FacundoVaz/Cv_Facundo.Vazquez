import pygame
import sys

from configuracion import*
from principal import*
from extras import*

def MENU():
    #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()

        #Preparar la ventana
        pygame.display.set_caption("Silabas...")
        screen = pygame.display.set_mode((ANCHO, ALTO))

        background=pygame.image.load("fondo2.jpg").convert()
        screen.blit(background,[0,-15])


        color_light = (170,170,170)

        color_dark = (100,100,100)

        defaultFont= pygame.font.Font( pygame.font.get_default_font(), 25)

        titulo=defaultFont.render('Cuánto sabes de la Copa América?' , True , COLOR_LETRAS)
        text = defaultFont.render('Iniciar' , True , COLOR_LETRAS)
        text2= defaultFont.render('Salir' , True , COLOR_LETRAS)
        background=pygame.image.load("fondo2.jpg")

        menu=True
        while menu:

            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:
                    pygame.quit()
                if ev.type==KEYDOWN:
                    if ev.key==K_ESCAPE:
                        pygame.quit()


                if ev.type == pygame.MOUSEBUTTONDOWN:

                    if 100 <= mouse[0] <= 240 and 500 <= mouse[1] <= 540:
                        main()
                    if 560 <= mouse[0] <= 700 and 500 <= mouse[1] <= 540:
                        pygame.quit()

            screen.blit(background,[0,0])

            mouse = pygame.mouse.get_pos()



            if 100 <= mouse[0] <= 240 and 500 <= mouse[1] <= 540:
                pygame.draw.rect(screen,color_light,[100,500,140,40])
            else:
               pygame.draw.rect(screen,color_dark,[100,500,140,40])

            if 560 <= mouse[0] <= 700 and 500 <= mouse[1] <= 540:
                pygame.draw.rect(screen,color_light,[560,500,140,40])
            else:
               pygame.draw.rect(screen,color_dark,[560,500,140,40])


            screen.blit(text ,(120,510))
            screen.blit(text2 ,(580,510))
            screen.blit(titulo ,(190,70))

            pygame.display.update()