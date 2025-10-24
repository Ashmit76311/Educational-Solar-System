"""
Educational Solar System (Modern Python/Pygame version)
-------------------------------------------------------
Author: Adapted by ChatGPT from original Turbo C++ BGI source
Run on: Windows/macOS/Linux
Requires: pygame (install via `pip install pygame`)
"""

import pygame
import math
import random
import sys

# Initialize pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Educational Solar System — Modern Version")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 204, 0)
WHITE = (255, 255, 255)
GREY = (169, 169, 169)
RED = (255, 80, 80)
BLUE = (80, 120, 255)
GREEN = (50, 220, 100)
ORANGE = (255, 165, 0)
PURPLE = (180, 100, 255)
CYAN = (80, 255, 255)
PINK = (255, 182, 193)

# Planet data: name, orbit radius, size, color, speed
planets = [
    ("Mercury", 60, 6, GREY, 0.04),
    ("Venus", 90, 8, ORANGE, 0.03),
    ("Earth", 120, 9, BLUE, 0.025),
    ("Mars", 160, 7, RED, 0.02),
    ("Jupiter", 220, 14, PINK, 0.015),
    ("Saturn", 280, 12, YELLOW, 0.012),
    ("Uranus", 340, 10, CYAN, 0.009),
    ("Neptune", 400, 9, PURPLE, 0.007),
    ("Pluto", 440, 4, WHITE, 0.006),
]

# Center of the solar system (sun)
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2

# For orbit animation
angles = [random.uniform(0, math.pi * 2) for _ in planets]
starfield = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(120)]

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 14)

def draw_sun():
    pygame.draw.circle(screen, YELLOW, (CENTER_X, CENTER_Y), 25)
    # simple pulsating glow
    glow = int(5 * math.sin(pygame.time.get_ticks() * 0.002)) + 25
    pygame.draw.circle(screen, (255, 220, 100), (CENTER_X, CENTER_Y), 25 + glow, 2)

def draw_orbits():
    for planet in planets:
        radius = planet[1]
        pygame.draw.circle(screen, (80, 80, 80), (CENTER_X, CENTER_Y), radius, 1)

def draw_planets():
    for i, (name, orbit, size, color, speed) in enumerate(planets):
        angles[i] += speed
        x = CENTER_X + int(orbit * math.cos(angles[i]))
        y = CENTER_Y + int(orbit * math.sin(angles[i]))
        pygame.draw.circle(screen, color, (x, y), size)
        if name == "Earth":
            # simple moon orbit
            mx = x + int(20 * math.cos(angles[i] * 5))
            my = y + int(20 * math.sin(angles[i] * 5))
            pygame.draw.circle(screen, GREY, (mx, my), 3)
        # show name label occasionally
        if random.random() < 0.005:
            text = font.render(name, True, WHITE)
            screen.blit(text, (x + 10, y))

def draw_spaceship():
    # simple triangle spaceship moving randomly
    t = pygame.time.get_ticks() * 0.001
    sx = WIDTH/2 + 250 * math.cos(t * 0.5)
    sy = HEIGHT/2 + 250 * math.sin(t * 0.5)
    points = [
        (sx, sy - 8),
        (sx - 10, sy + 8),
        (sx + 10, sy + 8),
    ]
    pygame.draw.polygon(screen, WHITE, points)

def main():
    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK)
        # stars
        for s in starfield:
            pygame.draw.circle(screen, WHITE, s, 1)
        draw_orbits()
        draw_sun()
        draw_planets()
        draw_spaceship()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()