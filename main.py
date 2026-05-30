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



OG_blackqueen = pygame.image.load("assets/B_Rook.bmp")
scaledQueen = pygame.transform.scale(OG_blackqueen , ( 80 , 80))

OG_blcackKnight = pygame.image.load("assets/B_Knight.bmp")
scaleB_Knight = pygame.transform.scale(OG_blcackKnight , (80 , 80 ))

OG_WightKnight = pygame.image.load("assets/W_Knight.bmp")
scaleW_Knight = pygame.transform.scale(OG_WightKnight , (70 , 70 ))


def pieces(P,currentX , currentY):
    match P:
        case "bR":
            screen.blit(scaledQueen , (currentX , currentY))
        case "bN":
            screen.blit(scaleB_Knight , (currentX , currentY))
        case "wN":
            screen.blit(OG_WightKnight , (currentX , currentY))

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
            else:
                pygame.draw.rect(screen, (118, 150, 86), (currentX , currentY , weigth ,height))
    
            pieces( Matrix[i][j] , currentX , currentY )

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