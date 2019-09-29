import pygame
import sys
import time

pygame.init()

resolution = (600, 600)
squares = 50

screen = pygame.display.set_mode(resolution)


class Snake:
    def __init__(self, segments, direction):
        self.segments = segments
        self.direction = direction

    def move_snake(self):

        if self.direction == "up":
            new_head = (self.segments[0][0], self.segments[0][1]-1)
            self.segments.insert(0, new_head)
            self.segments.pop()


start_pos = [(squares/2, squares/2), (squares/2, (squares/2)+1), (squares/2, (squares/2)+2)]
snake = Snake(start_pos, "up")


while True:
    time.sleep(0.1)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

    snake.move_snake()

    screen.fill((0, 0, 0))

    for segment in snake.segments:

        pos = ((segment[0]/squares)*resolution[0], (segment[1]/squares)*resolution[0],
               resolution[0]/squares, resolution[1]/squares)

        pygame.draw.rect(screen, (255, 255, 255), pos)

    pygame.display.flip()
