import pygame
import math
import sys
import random

s = [1000, 800]

pygame.init()
screen = pygame.display.set_mode(s, 0, 32)
pygame.display.set_caption("Pi to 1 billion digits")

current = [int(i/2) for i in s]
magnification = 0.8

pairs = {i: i*36 for i in range(10)}
colours = {i: tuple(random.randint(0, 255) for _ in range(3)) for _ in range(10)}
font = pygame.font.SysFont("Garamond MS", 20)

screen.fill((0, 0, 0))

def heading(deg):
    return [math.cos(math.radians(deg)), math.sin(math.radians(deg))]

with open("digits.txt", "r") as f:
    for pos, digit in enumerate(f.read()):
        try:
            digit = int(digit)
        except:
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, (0, 0, 0), [0, 0, 200, 25], 0)
        msg = font.render(f"Digit {pos}: {digit}", True, (255, 255, 255))
        screen.blit(msg, (10, 10))
        
        new = [current[i] + [j*2 for j in heading(pairs[int(digit)])][i] for i in range(2)]
        pygame.draw.line(screen, colours[int(digit)], current, new, 1)
        current = new

        pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
