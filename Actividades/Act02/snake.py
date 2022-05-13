"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
import random

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

"""Definimos los colores"""
colors = ["blue", "green", "purple", "black", "orange"]
bodyColor = colors[random.randint(0,4)]
foodColor = colors[random.randint(0,4)]

"""Se crea condicional para que el cuerpo y la comida tengan diferente color"""
while foodColor == bodyColor:
    foodColor = colors[random.randint(0,4)]


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)
