import pygame
import time
import random

#defini a velocidade do player
snake_speed = 20

#defini o tamanho da janela que vai ser aberta 
window_x = 720
window_y = 480

#defini o RGB do jogo 
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


pygame.init()


pygame.display.set_caption('GeeksforGeeks Snakes')
game_window = pygame.display.set_mode((window_x, window_y))


fps = pygame.time.Clock()


snake_position = [100, 50]

#defini o corpo da cobra
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
#defini a posição da "fruta" aleatoriamente 
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True


direction = 'RIGHT'
change_to = direction

#aqui define a pontuação inicial
score = 0



def show_score(choice, color, font, size):

    score_font = pygame.font.SysFont(font, size)

#Aqui mostra a pontuação final 
    score_surface = score_font.render('PONTUAÇÃO : ' + str(score), True, color)


    score_rect = score_surface.get_rect()


    game_window.blit(score_surface, score_rect)



def game_over():
    #defini a fonte do texto
    my_font = pygame.font.SysFont('times new roman', 50)

    #Mostra a pontuação atual
    game_over_surface = my_font.render(
        'SUA PONTUAÇÃO : ' + str(score), True, green)


    game_over_rect = game_over_surface.get_rect()


    game_over_rect.midtop = (window_x / 2, window_y / 4)


    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

#depois de 4 segundos o jogo vai sair
    time.sleep(4)

#fecha as bibliotecas 
    pygame.quit()

#obviamente sair do programa 
    quit()


#Aqui é o Main
while True:


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

#aqui diz que não pode pressionar duas teclas simultaneamente 
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

#se a cobra e a fruta estão colidindo estamos aumentando essa pontuação em 1 ponto 
    if direction == 'UP':
        snake_position[1] -= 1
    if direction == 'DOWN':
        snake_position[1] += 1
    if direction == 'LEFT':
        snake_position[0] -= 1
    if direction == 'RIGHT':
        snake_position[0] += 1

#verifica se a cobra bateu na parede
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, red,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

#se a cobra colidir vai dar game over, aqui seriam as condições dos jogos 
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()


    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

#Aqui mostra a pontuação final 
    show_score(1, white, 'times new roman', 20)


    pygame.display.update()


    fps.tick(snake_speed)
