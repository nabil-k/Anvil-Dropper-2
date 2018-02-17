import cx_Freeze
import sys
import random
import pygame
import time

pygame.mixer.init()
pygame.font.init()


# Comic Sans Font
Csf = pygame.font.SysFont('Anton-Regular.ttf', 61)

pygame.mixer.music.load('Balloon-Game.mp3')
pygame.mixer.music.play(loops = 0, start = 0.0)


# Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

pygame.display.set_caption("Anvil Dropper")
pygame.display.set_icon(pygame.image.load("anvil.png"))

width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

gameRun = True

playerScore = 1

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
        menuBg = pygame.image.load("menuWallpaper.png")
        screen.blit(menuBg, (0,0))
        pygame.display.update()
        fpsClock.tick(15)

def gameOver():
    global playerScore
    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
                print("Game Has Restarted")
                playerScore = 1
                gameLoop()
        screen.blit(pygame.image.load("gameOverBg.png"),(0,0))
        largeText = pygame.font.Font('Anton-Regular.ttf',34)
        playerScoreText = Csf.render("Score: " + str(round(playerScore, 0)), False, (255, 0, 255))
        screen.blit(playerScoreText,(1000,10))
        pygame.display.update()
        fpsClock.tick(15)
            

# Player (Player playing as "Blue")
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("blue.png"), (120,120))
        self.rect = self.image.get_rect()
        self.rect.x = 540
        self.rect.y = 500
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
             self.rect.x -= 10
        if key[pygame.K_RIGHT]:
             self.rect.x += 10

    def render(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
player = Player(0,0)

class Anvil():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("anvil.png"), (120,120))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0
    def update(self):
        self.rect.y += 15
        if anvil.rect.colliderect(player.rect):
            print("anvil hit player")
            gameOver()
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
    global playerScore
    while gameRun:
        
        t1 = time.time()
        dt = t1 - t0
        screen.blit(pygame.image.load("gameBg.png"),(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRun = False
                sys.exit()
          
        # Adds Anvil Every 3 Seconds
        anvilCounter = 0
        if dt >= 2:
            newX = random.randint(1,1280)
            print ("Anvil Spawnd At X Cord:",newX)
            anvil.rect.x = newX
            print ("2 seconds reached, resetting timer")
            anvils.append(anvil)
            t0 = t1
            print(anvils)
            

        for anvil in anvils:
            print("Anvil Y Cord:",anvil.rect.y)
            if anvil.rect.y >= 500:
                anvil.rect.y = 0
                anvils.remove(anvils[0])
        
            anvil.update()
            anvil.render(screen)

        playerScore += pygame.time.get_ticks() /100000
        print(playerScore)
        playerScoreText = Csf.render("Score: " + str(round(playerScore, 0)), False, (0, 255, 0))
        screen.blit(playerScoreText,(1000,10))
        # Update.
        player.update()
        # Draw.
        player.render(screen) 
            
        
        
        pygame.display.flip()
        fpsClock.tick(fps)

StartMenu()

