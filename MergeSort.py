import pygame
import VisCom
import math
width = 800
finished = False
number_of_pixels = 500  # total number of pixels in a row, the number of elements to sort is half of it
pixel_width = int(width / number_of_pixels)



list_to_sort = [None for i in range(0,int(number_of_pixels/2))] # containts the start position of the line and the number which the line represents (x,y, factor)
delay = int(1/number_of_pixels * 4000)


clock = None
SCREEN = None


def set_window(name):
    global SCREEN
    pygame.init()
    clock = pygame.time.Clock()
    clock.tick(30)
    SCREEN = pygame.display.set_mode(size=(width, width))
    pygame.display.set_caption(name)
def set_data_size(data_size):
    global number_of_pixels
    global width
    global pixel_width
    global list_to_sort
    global delay
    global SCREEN
    number_of_pixels = 2 * data_size
    if number_of_pixels >= 400:
        number_of_pixels = 400
        width = 800
    elif width % number_of_pixels != 0:
        old_pixel_width = int(VisCom.round(width/ number_of_pixels))
        width = old_pixel_width * number_of_pixels
    pixel_width = int(width / number_of_pixels)
    list_to_sort = [None for i in range(0, int(number_of_pixels/2))]
    delay = int(1 / number_of_pixels * 3000)
    SCREEN = pygame.display.set_mode(size=(width, width))
def program_loop():
    global finished
    SCREEN.fill(VisCom.Colors.WHITE)
    VisCom.draw_lines(SCREEN, VisCom.Colors.BLACK, pixel_width, width, number_of_pixels, list_to_sort)
    pygame.display.update()
    sort_start = False
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                pygame.quit()
                #quit()
            if (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN) and not sort_start:
                mergeSort(list_to_sort)
                sort_start = True
        if not finished:
            pygame.display.update()
def mergeSort(lst):
    if len(lst) > 1:

        # Finding the mid of the array
        mid = len(lst) // 2

        # Dividing the array elements
        L = lst[:mid]

        # into 2 halves
        R = lst[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i][2] < R[j][2]:
                assign(SCREEN, width, pixel_width, lst,L, k, i)#lst[k] = L[i]
                pygame.time.delay(delay)
                pygame.display.update()
                i += 1
            else:
                assign(SCREEN, width, pixel_width, lst, R, k,j)#lst[k] = R[j]
                pygame.time.delay(delay)
                pygame.display.update()
                j += 1
            k += 1
        #pygame.time.delay(delay)
        #pygame.display.update()
        # Checking if any element was left
        while i < len(L):
            assign(SCREEN, width, pixel_width, lst, L, k , i)#lst[k] = L[i]
            pygame.time.delay(delay)
            pygame.display.update()
            i += 1
            k += 1
        #pygame.time.delay(delay)
        #pygame.display.update()
        while j < len(R):
            assign(SCREEN, width, pixel_width, lst, R, k , j)#lst[k] = R[j]
            pygame.time.delay(delay)
            pygame.display.update()
            j += 1
            k += 1
        #pygame.time.delay(delay)
        #pygame.display.update()
def assign(Surface, screenWidth, pixelWidth, lst1,lst2, u, v):
    pygame.draw.line(Surface, VisCom.Colors.WHITE, (lst1[u][0], 0), (lst1[u][0], screenWidth),pixelWidth)
    #remove the whole column

    lst1[u]= [lst1[u][0], lst1[u][1], lst2[v][2]]
    pygame.draw.line(Surface, VisCom.Colors.BLACK, (lst1[u][0], screenWidth - lst1[u][2] * pixelWidth), (lst1[u][0], screenWidth),pixelWidth)
    #draw the new column
