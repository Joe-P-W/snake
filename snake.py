import pygame
import sys
import time
import random

pygame.init()

resolution = (600, 600)
squares = 20
green = (0, 255, 0) 
blue = (0, 0, 128) 
score = 0

screen = pygame.display.set_mode(resolution)
font = pygame.font.SysFont('Arial', 30)

def check_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if snake.direction != "right":
                    snake.direction = "left"
                    break
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if snake.direction != "left":
                    snake.direction = "right"
                    break
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if snake.direction != "up":
                    snake.direction = "down"
                    break
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                if snake.direction != "down":
                    snake.direction = "up"
                    break


class Snake:
    def __init__(self, segments, direction):
        self.segments = segments
        self.direction = direction

    def move_snake(self, apple_pos):

        if self.direction == "up":
            new_head = (self.segments[0][0], self.segments[0][1]-1)
            self.segments.insert(0, new_head)
            if apple_pos != self.segments[0]:
                self.segments.pop()

        elif self.direction == "down":
            new_head = (self.segments[0][0], self.segments[0][1]+1)
            self.segments.insert(0, new_head)
            if apple_pos != self.segments[0]:
                self.segments.pop()

        elif self.direction == "left":
            new_head = (self.segments[0][0]-1, self.segments[0][1])
            self.segments.insert(0, new_head)
            if apple_pos != self.segments[0]:
                self.segments.pop()

        elif self.direction == "right":
            new_head = (self.segments[0][0]+1, self.segments[0][1])
            self.segments.insert(0, new_head)
            if apple_pos != self.segments[0]:
                self.segments.pop()
    
    def check_out_of_bounds(self):
        
        for segment in self.segments:
            if segment[0] < 0 or segment[0] > squares-1 or segment[1] < 0 or segment[1] > squares-1:
                return True
        for i in range(len(self.segments)):
            if self.segments[i] in self.segments[:i]:
                return True
            if self.segments[i] in self.segments[:i]:
                return True
        
        return False
        

class Apple:
    def __init__(self, pos):
        self.pos = pos
    
    def check_if_eaten(self, snake_pos, score, snake_segments):
        if snake_pos == self.pos:

            while self.pos in snake_segments:
                self.pos = (random.randint(0,squares - 1),random.randint(0,squares - 1))

            score += 1
            return score
        else:
            return score
            

start_pos = [(squares/2, squares/2), (squares/2, (squares/2)+1), (squares/2, (squares/2)+2)]
snake = Snake(start_pos, "up")

apple_start = (random.randint(0,squares-1),random.randint(0,squares-1))
while apple_start in start_pos:
    apple_start = (random.randint(0,squares-1),random.randint(0,squares-1))
    
apple = Apple(apple_start)


while True:
    time.sleep(0.15)
    check_events()
    snake.move_snake(apple.pos)
    score = apple.check_if_eaten(snake.segments[0], score, snake.segments)
    out_of_bounds = snake.check_out_of_bounds()
    
    screen.fill((0, 0, 0))


    if not out_of_bounds:
        
        apple_pos = ((apple.pos[0]/squares)*resolution[0], (apple.pos[1]/squares)*resolution[0],
                resolution[0]/squares, resolution[1]/squares)
                
        pygame.draw.rect(screen, (255, 0, 0), apple_pos)
        
        for segment in snake.segments:

            pos = ((segment[0]/squares)*resolution[0], (segment[1]/squares)*resolution[0],
                   resolution[0]/squares, resolution[1]/squares)

            pygame.draw.rect(screen, (255, 255, 255), pos)
            
        text = font.render(f'Score: {score}', False, (255, 0, 255))
        screen.blit(text, (resolution[0]-150, 10))
        
    else:
        break

    pygame.display.flip()

while True:
    text = font.render('Game Over', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (resolution[0] // 2, resolution[1] // 2)
    screen.blit(text, textRect)
    check_events()
    pygame.display.flip()

