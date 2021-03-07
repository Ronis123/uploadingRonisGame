import pygame
from random import randint
pygame.init()

x = 400 
y = 100
pos_x = 526
pos_y = 800  #carro azul
pos_y_a = 800
pos_y_c = 3000 #carroamarelo

timer = 0
tempo_segundo = 0

velocidade_outros = 12

velocidade = 30


fundo = pygame.image.load("fundo.jpg")
samuel = pygame.image.load("samuel.jpg")
carroazul = pygame.image.load("carroazul.jpg")
carroamarelo = pygame.image.load("carroamarelo.jpg")
carroverde = pygame.image.load("carroverde.jpg")
chorao = pygame.image.load("face.jpg")


font = pygame.font.SysFont("arial black",30) 
texto = font.render("Tempo: ", True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center=(40,32)


janela=pygame.display.set_mode((800,600))
pygame.display.set_caption("Criando um jogo com python")

janela_aberta=True

while janela_aberta:
    pygame.time.delay(50)
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    chorao = pygame.image.load ("face.jpg")

    if comandos[pygame.K_RIGHT] and x <= 540:
        x += velocidade
    if comandos[pygame.K_LEFT] and x >= 140: 
        x -= velocidade



  #verifica a colisao
    if ((x + 80 > pos_x and y + 180 > pos_y) ):
        y = 1200
        print(chorao)

    if ((x - 80 < pos_x - 300 and y + 180 > pos_y_a)):
        y = 1200
        print(chorao)

    if ((x + 80 > pos_x - 136 and y + 180 > pos_y_c)) and ((x - 80 < pos_x - 136 and y + 180 > pos_y_c)):
        y = 1200
        print(chorao)



    if (pos_y <= -180):
         pos_y = randint(800,1000)

    if(pos_y_a <= -180):
        pos_y_a = randint(1200,2000)

    if (pos_y_c <= -180):
         pos_y_c = randint(2200,3000)


    if (timer < 20):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (255,255,255), (0,0,0))
        time = 0

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +2
    pos_y_c -= velocidade_outros +10 #carro amarelo

    janela.blit(fundo, (0,0))
    janela.blit(samuel, (x,y))
    janela.blit(carroazul, (pos_x, pos_y))
    janela.blit(carroverde, (pos_x - 380, pos_y_a))
    janela.blit(carroamarelo, (pos_x - 160, pos_y_c))
    janela.blit(texto, pos_texto)

    

    

    pygame.display.update()



pygame.quit()
