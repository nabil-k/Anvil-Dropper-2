import sys
import random
import pygame
import time

pygame.mixer.init()
pygame.mixer.music.load('./assets/Balloon Game.mp3')
pygame.mixer.music.play(loops = 0, start = 0.0)


# Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

gameRun = True

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def StartMenu():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                    
                    print("Game Has Now Begun")
                    gameLoop()
                
        screen.fill(white)
        largeText = pygame.font.Font('./assets/Anton-Regular.ttf',115)
        menuBg = pygame.image.load("./assets/menuWallpaper.png")
        screen.blit(menuBg, (-20,-20))
        TextSurf, TextRect = text_objects("Anvil Dropper", largeText)
        TextRect.center = ((width/2),(height/2))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        fpsClock.tick(15)
            

# Player (Player playing as "Blue")
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("./assets/blue.png"), (120,120))
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 500
        self.velocity = 0
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
             self.rect.x -= 20
        if key[pygame.K_RIGHT]:
             self.rect.x += 20

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
player = Player(0,0)

class Anvil():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("./assets/anvil.png"), (120,120))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = 0
        self.velocity = 0
    def update(self):
        self.rect.y += 1
    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
anvil = Anvil(0,0)

# Game loop

t0 = time.time()
anvils = []
def gameLoop():
    global gameRun
    global t0
    global anvil
    global anvils
    while gameRun:
        
        t1 = time.time()
        dt = t1 - t0
        screen.blit(pygame.image.load("./assets/gameBg.png"),(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRun = False
                sys.exit()
          
        # Adds Anvil Every 3 Seconds
        if dt >= 2:
            print(dt)
            newX = random.randint(1,1280)
            print ("Anvil Spawnd At X Cord:",newX)
            anvil.x = newX
            print ("Three seconds reached, resetting timer")
            anvils.append(anvil)
            t0 = t1
            print(anvils)
            
            
        anvil.update()
        anvil.render(screen)
        for anvil in anvils:
            if player.rect.colliderect(anvil.rect):
                print("you touched me")
            if anvil.y >= 510:
                anvil.y = 0
                anvils.remove(anvils[0])

        
            
            
        
        


        # Update.
        player.update()
        # Draw.
        player.render(screen) 
            
        
        
        pygame.display.flip()
        fpsClock.tick(fps)

StartMenu()

