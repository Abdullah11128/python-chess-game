import pygame


pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
running = True


def BoardInit(): # to init the board outside of the game loop 
    
    weigth = 80 
    height = 80

    for i in range(8):

        currentX = i * 80
        currentY = i * 80

        if i % 2 == 0: # even
            pygame.draw.rect(screen, "black", (currentX , currentY , weigth ,height))
        else:
            pygame.draw.rect(screen, "white", (currentX , currentY , weigth ,height))
        



while running:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")
    BoardInit()
    
    pygame.display.flip()

    clock.tick(60)  # FPS 

pygame.quit()