import pygame


pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
running = True

Matrix = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],  
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],  
    ["--", "--", "--", "--", "--", "--", "--", "--"],  
    ["--", "--", "--", "--", "--", "--", "--", "--"],  
    ["--", "--", "--", "--", "--", "--", "--", "--"],  
    ["--", "--", "--", "--", "--", "--", "--", "--"],  
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]



OG_blackqueen = pygame.image.load("assets/Chess_queenB.bmp")
scaledQueen = pygame.transform.scale(OG_blackqueen , (70 , 70))

def BoardInit(): # to init the board outside of the game loop 
    
    weigth = 80 
    height = 80
    currentX = 0
    currentY = 0
    switch1=1

    for i in range(8):
        currentX = 0
        switch1+=1

        for j in range(8):
            if  switch1%2==0: # even
                pygame.draw.rect(screen, (240, 217, 181), (currentX , currentY , weigth ,height))
            
            if Matrix[i][j] == "bR":
                    screen.blit(scaledQueen , (currentX , currentY))
            else:
                pygame.draw.rect(screen, (118, 150, 86), (currentX , currentY , weigth ,height))

            currentX += 80
            switch1+=1
    
        currentY += 80
    



while running:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")
    BoardInit()

    
    pygame.display.flip()

    clock.tick(60)  # FPS 

pygame.quit()
