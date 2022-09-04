#This File is needed to Visualize the Algorithms
import pygame
from random import randrange
import math
class Colors:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0,0,255)
    GREEN = (144,238,144)
class Pixel:
    def __init__(self, Surface, color, screenWidth, pixelWidth ,pixelNumber, col, row):
        self.Surface = Surface
        self.color = color
        self.screenWidth = screenWidth
        self.pixelWidth = pixelWidth
        self.pixelNumber = pixelNumber
        self.col = col
        self.row = row

#draw_lines draws random lines on the screen and saves them in the given lst
#the amount of lines depends on the number of Pixels
def draw_lines(Surface, color, pixelWidth, widthOfScreen, pixelNumber, lst):
    offset =0
    for i in range(0, int(pixelNumber / 2) ):
        # pixelNumber represents the total number of pixels in a row, so the total number of lines is half of it
        factor = randrange(1,pixelNumber)
        pygame.draw.line(Surface, color, (int(offset + pixelWidth + int(pixelWidth/2)), int(widthOfScreen - factor * pixelWidth)), (int(offset + pixelWidth + int(pixelWidth/2)), widthOfScreen), int(pixelWidth) )
        lst[i] = [offset + pixelWidth + int(pixelWidth/2), widthOfScreen - factor * pixelWidth, factor]
        #each element of lst contains the start position of the line and the length of the line in pixel widths
        offset += 2 * pixelWidth

# The Method "swap" takes a list and two indexes to swap the elements in the list and display the new lines on the screen
def swap(Surface, screenWidth, pixelWidth,lst,u ,v):

    pygame.draw.line(Surface, Colors.WHITE, (lst[u][0], screenWidth - lst[u][2] * pixelWidth), (lst[u][0], screenWidth), pixelWidth)
    pygame.draw.line(Surface, Colors.WHITE, (lst[v][0], screenWidth - lst[v][2] * pixelWidth), (lst[v][0], screenWidth), pixelWidth)

    cop  = lst[u][2]
    lst[u][2] = lst[v][2]
    lst[v][2] = cop

    pygame.draw.line(Surface, Colors.BLACK, (lst[u][0], screenWidth - lst[u][2] * pixelWidth), (lst[u][0], screenWidth), pixelWidth)
    pygame.draw.line(Surface, Colors.BLACK, (lst[v][0], screenWidth - lst[v][2] * pixelWidth), (lst[v][0], screenWidth), pixelWidth)
def round(number):
    if number - math.floor(number) < 0.5:
        return math.floor(number)
    return math.ceil(number)