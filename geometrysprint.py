import pygame
import random
from pygame import mixer

        ######################################################

mixer.init()
mixer.music.load('gsmenuloop.mp3')
screen = pygame.display.set_mode((1600, 900))
trailsurface = pygame.Surface((10, 30), pygame.SRCALPHA)
screen.fill((0, 200, 255))
mdown = False
clock = pygame.time.Clock()
boxy = 450
boxvely = 0
shiprotation = 20
ship = pygame.image.load("shipppp.png")
pfp = pygame.image.load("geometrysprintnew.png")
pygame.display.set_caption("Geometry Sprint")
pygame.display.set_icon(pfp)
shiprect = ship.get_rect()
gamemode = ""
ball = pygame.image.load("balls.png")
spider = pygame.image.load("spider.png")
spiderflipped = pygame.image.load("spiderflip.png")
wave = pygame.image.load("wave.png")
swing = pygame.image.load("swingo.png")
ufo = pygame.image.load("ufo.png")
cube = pygame.image.load("cube.png")
playbutton = pygame.image.load("playbutton.png")
block1 = pygame.image.load("block.png")
block2  = pygame.image.load("block.png")
block3 = pygame.image.load("block.png")
logo = pygame.image.load("gslogo.png")
uforect = ufo.get_rect()
swingrect = swing.get_rect()
block1x = 1600
block2x = 2133
block3x = 2666
block1y = random.randint(3, 20)*45-122
block2y = random.randint(3, 20)*45-122
block3y = random.randint(3, 20)*45-122
cuberect = cube.get_rect()
oldrot = 0
newrot = 0
prevposs = []
mouseX = 0
mouseY = 0
length = 0
cd = 0
rotationleft = 0
normgrav = True

        ######################################################

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mdown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mdown = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                gamemode = "ship"
                shiprotation = 20
            if event.key == pygame.K_w:
                gamemode = "wave"
            if event.key == pygame.K_u:
                gamemode = "ufo"
            if event.key == pygame.K_g:
                gamemode = "swing"
                normgrav = True
            if event.key == pygame.K_p:
                gamemode = "spider"
                normgrav = True
            if event.key == pygame.K_c:
                gamemode = "cube"
                rotationleft = 0
    if gamemode == "" and mdown:
        if mouseX < 900 and mouseX > 600 and mouseY < 700 and mouseY > 400: # play + music
            gamemode = "ship"
            #mixer.music.set_volume(0.1)
            #mixer.music.play()
            
        ######################################################
            
    if gamemode == "ship":
        
        if not mdown: # up/down
            boxvely -= 0.9
        elif mdown:
            boxvely += 0.9
            
        if boxvely >= 20: # speed cap
            boxvely = 20
        elif boxvely <= -20:
            boxvely = -20

        boxy -= boxvely
        newrot = 1.5*boxvely + 20
        rotatedship = pygame.transform.rotate(ship, boxvely * 2)
        
        if boxy <= 55: # bounds
            boxy = 56
            boxvely = 0
            rotatedship = pygame.transform.rotate(ship, boxvely * 2+1.5)
        if boxy >= 844:
            rotatedship = pygame.transform.rotate(ship, boxvely * 2+1.5)
            boxy = 843
            boxvely = 0

        screen.fill((0, 200, 255))
        prevposs.append(boxy)

        rotatedrect = rotatedship.get_rect(center=shiprect.center) # rot ship
        
        if len(prevposs) < 30:
            for i in range(len(prevposs)):
                pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                screen.blit(trailsurface, (380 - (i * 10), prevposs[-i-1]))
        else:
            for i in range(30):
                pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                screen.blit(trailsurface, (380 - (i * 10), prevposs[-i-1]))
                
        # draw the gm
        screen.blit(rotatedship, (400 - rotatedrect.width // 2, boxy - rotatedrect.height // 2))

            
        ######################################################

    if gamemode == "wave":
        
        if not mdown:
            boxy += 15
        elif mdown:
            boxy -= 15

        rotatedwave = pygame.transform.rotate(wave, -(oldrot))
        oldrot = newrot
        
        if mdown: # rotation
            rotatedwave = pygame.transform.rotate(wave, 45)
        elif not mdown:
            rotatedwave = pygame.transform.rotate(wave, -45)
            
        if boxy <= -30: # bounds
            boxy = -29
            rotatedwave = pygame.transform.rotate(wave, 0) # fixes bug
            oldrot = newrot
            
        if boxy >= 844:
            boxy = 843
            rotatedwave = pygame.transform.rotate(wave, 0) # fixes bug
            oldrot = newrot
            
        prevposs.append(boxy)
        screen.fill((0, 200, 255))

        if len(prevposs) < 30:
            for i in range(len(prevposs)):
                pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                screen.blit(trailsurface, (430 - (i * 10), prevposs[-i-1]+40))
        else:
            for i in range(30):
                pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                screen.blit(trailsurface, (430 - (i * 10), prevposs[-i-1]+40))
                
        screen.blit(rotatedwave, (400, boxy))

                ######################################################
        
    if gamemode == "ufo":
        
        if not mdown and boxy < 770:
            boxvely -= 0.8
        elif mdown:
            boxvely = 15

        oldrot = newrot

        if mdown: # rotation
            rotatedufo = pygame.transform.rotate(ufo, -20)
            cd = 15
            mdown = False
        elif not mdown and cd <= 0:
            rotatedufo = pygame.transform.rotate(ufo, 0)

        if boxvely >= 20:
            boxvely = 20
        elif boxvely <= -20:
            boxvely = -20

        if boxy <= -30: # bounds
            boxy = -29
            boxvely = 0

        if boxy >= 771:
            boxy = 770
            boxvely = 0

        cd -= 1

        boxy -= boxvely
        prevposs.append(boxy)
        screen.fill((0, 200, 255))

        if len(prevposs) >= 30:
            for i in range(30):
                pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                screen.blit(trailsurface, (430 - (i * 10), prevposs[-i-1]+80))

        else:
            for i in range(len(prevposs)):
                pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                screen.blit(trailsurface, (430 - (i * 10), prevposs[-i-1]+80))

        rotatedrect = rotatedufo.get_rect(center=uforect.center) # rot ufo
        screen.blit(rotatedufo, (470 - rotatedrect.width // 2, (boxy+70) - rotatedrect.height // 2))

            ######################################################

    if gamemode == "swing":
        
        if mdown:
            if normgrav:
                normgrav = False
            else:
                normgrav = True
            mdown = False
                
        if boxvely >= 20: # speed cap
            boxvely = 20
        elif boxvely <= -20:
            boxvely = -20
            
        if normgrav:
            boxvely -= 0.8
        else:
            boxvely += 0.8
            
        boxy -= boxvely
        newrot = 1.5*boxvely + 20
        
        rotatedswing = pygame.transform.rotate(swing, boxvely * 2)
        
        if boxy <= 55: # bounds
            boxy = 56
            boxvely = 0
            rotatedswing = pygame.transform.rotate(swing, boxvely * 2+1.5)
        if boxy >= 844:
            rotatedswing = pygame.transform.rotate(swing, boxvely * 2+1.5)
            boxy = 843
            boxvely = 0

        screen.fill((0, 200, 255))
        prevposs.append(boxy)

        rotatedrect = rotatedswing.get_rect(center=swingrect.center) # rot ship
        
        if len(prevposs) < 30:
            for i in range(len(prevposs)):
                pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                screen.blit(trailsurface, (380 - (i * 10), prevposs[-i-1]))
        else:
            for i in range(30):
                pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                screen.blit(trailsurface, (380 - (i * 10), prevposs[-i-1]))
                
        # draw the gm
        screen.blit(rotatedswing, (400 - rotatedrect.width // 2, boxy - rotatedrect.height // 2))

        #######################################################

    if gamemode == "spider":
        
        if mdown:
            if normgrav:
                for i in range(10):
                    prevposs.append(700-(70*i))
                normgrav = False
            else:
                for i in range(10):
                    prevposs.append(70*i)
                normgrav = True
            mdown = False

        if normgrav:
            boxy = 770
        else:
            boxy = 0

        prevposs.append(boxy)
        screen.fill((0, 200, 255))
        
        if len(prevposs) >= 30:
            for i in range(30):
                if normgrav:
                    pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                    screen.blit(trailsurface, (430 - (i * 10), prevposs[-i-1]+80))
                else:
                    pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                    screen.blit(trailsurface, (430 - (i * 10), prevposs[-i-1]+40))
        else:
            for i in range(len(prevposs)):
                if normgrav:
                    pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                    screen.blit(trailsurface, (430 - (i * 10), prevposs[-i-1]+80))
                else:
                    pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                    screen.blit(trailsurface, (430 - (i * 10), prevposs[-i-1]+40))
                
        if normgrav:
            screen.blit(spider, (400, boxy))
        else:
            screen.blit(spiderflipped, (400, boxy))

        ######################################################

    if gamemode == "cube":

        if mdown and boxy > 769:
            boxvely = 20
            rotationleft = 180
        else:
            boxvely -= 1.2

        boxy -= boxvely

        if boxy <= -30: # bounds
            boxy = -29
            boxvely = 0

        if boxy >= 771:
            boxy = 770
            boxvely = 0
            
        rotationleft -= 6
        
        if rotationleft < 0:
            rotationleft = 0
            
        rotatedcube = pygame.transform.rotate(cube, rotationleft)
        prevposs.append(boxy)
        screen.fill((0, 200, 255))

        if len(prevposs) >= 30:
            for i in range(30):
                pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                screen.blit(trailsurface, (430 - (i * 10), prevposs[-i-1]+80))

        else:
            for i in range(len(prevposs)):
                pygame.draw.rect(trailsurface, (255, 255, 255, 255 - (i * 8.5)), (0, 0, 10, 30)) # trail
                screen.blit(trailsurface, (430 - (i * 10), prevposs[-i-1]+80))

        rotatedrect = rotatedcube.get_rect(center=cuberect.center) # rot cube
        screen.blit(rotatedcube, (470 - rotatedrect.width // 2, (boxy+70) - rotatedrect.height // 2))

        ####################################################
        
    mousepos = pygame.mouse.get_pos() # mouse pos
    mouseX, mouseY = mousepos

    block1x -= 10
    block2x -= 10
    block3x -= 10

    if gamemode != "":
        if block1x <= -122: ## respawn block
            block1x = 1600
            block1y = random.randint(3, 20)*45-122
        if block2x <= -122:
            block2x = 1600
            block2y = random.randint(3, 20)*45-122
        if block3x <= -122:
            block3x = 1600
            block3y = random.randint(3, 20)*45-122

        screen.blit(block1, (block1x, block1y))
        screen.blit(block2, (block2x, block2y))
        screen.blit(block3, (block3x, block3y))

    if gamemode == "": # render play button
        screen.blit(playbutton, (620, 400))
        screen.blit(logo, (20, 100))

    pygame.display.flip()
    clock.tick(60)
