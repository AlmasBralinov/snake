import pygame
from random import randint

pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake')

def spawn_apple():
    x = randint(0, (size[0] / obj_size[0]) - 1)
    y = randint(0, (size[1] / obj_size[1]) - 1)
    return (x * obj_size[0], y * obj_size[1])

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

def move_snake():
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
        
    if snake_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - obj_size[1])
    if snake_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + obj_size[1])
    if snake_direction == RIGHT:
        snake[0] = (snake[0][0] + obj_size[0], snake[0][1])
    if snake_direction == LEFT:
        snake[0] = (snake[0][0] - obj_size[0], snake[0][1])    

obj_size = (10, 10)
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

snake = [(0, 0), (0 + obj_size[0], 0), (0 + 2 * obj_size[0], 0)]
snake_part = pygame.Surface(obj_size)
snake_part.fill((0, 0, 0))

apple_pos = spawn_apple()
apple = pygame.Surface(obj_size)
apple.fill((0, 0, 0))

snake_direction = RIGHT

clock = pygame.time.Clock()

font = pygame.font.Font('freesansbold.ttf', 18)
score = 0
fps = 20

score_font = font.render('Score: ' + str(score), True, (0, 0, 0))
score_rect = score_font.get_rect()
score_rect.topleft = (size[0] - 100, 10)

game_over = False

def spawn_apple():
    x = randint(0, (size[0] / obj_size[0]) - 1)
    y = randint(0, (size[1] / obj_size[1]) - 1)
    return (x * obj_size[0], y * obj_size[1])


def collision(pos1, pos2):
    return (pos1[0] == pos2[0]) and (pos1[1] == pos2[1])


def move_snake():
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])
        
    if snake_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - obj_size[1])
    elif snake_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + obj_size[1])
    elif snake_direction == RIGHT:
        snake[0] = (snake[0][0] + obj_size[0], snake[0][1])
    elif snake_direction == LEFT:
        snake[0] = (snake[0][0] - obj_size[0], snake[0][1])    


while not game_over:

    score_font = font.render('Score: ' + str(score), True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            if event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            if event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            if event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = spawn_apple()
        snake.append((0, 0))
        score = score + 1
        
    if snake[0][0] >= size[0] or snake[0][1] >= size[1] or snake[0][0] < 0 or snake[0][1] < 0:
        game_over = True
    
    move_snake()
    
    for i in range(1, len(snake) - 1):
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            game_over = True
    
    clock.tick(fps)
    screen.fill((51, 153, 51))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_part, pos)
    screen.blit(score_font, score_rect)
    
    pygame.display.flip()
    
pygame.quit()