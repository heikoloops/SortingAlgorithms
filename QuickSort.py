import pygame
import VisCom

width = 800
finished = False
number_of_pixels = 800  # total number of pixels in a row, the number of elements to sort is half of it
pixel_width = int(width / number_of_pixels)



list_to_sort = [None for i in range(0, int(number_of_pixels / 2))]  # containts the start position of the line and the value of the line (x,y, factor)
delay = int(1/number_of_pixels * 8000)



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
        old_pixel_width = int(VisCom.round(width / number_of_pixels))
        width = old_pixel_width * number_of_pixels
    pixel_width = int(width / number_of_pixels)
    list_to_sort = [None for i in range(0, int(number_of_pixels/2))]
    delay = int(1 / number_of_pixels * 8000)
    SCREEN = pygame.display.set_mode(size=(width, width))
def program_loop():
    global finished
    SCREEN.fill(VisCom.Colors.WHITE)
    VisCom.draw_lines(SCREEN, VisCom.Colors.BLACK, pixel_width, width, number_of_pixels, list_to_sort)
    pygame.display.update()
    sort_start = False
    l_list = 0
    r_list = len(list_to_sort) -1
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                pygame.quit()
                #quit()
            if (event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN) and not sort_start:
                sort_start = True
                quick_sort(SCREEN, width, pixel_width, list_to_sort,l_list, r_list )

        if not finished:
            pygame.display.update()


def quick_sort(Surface, screenWidth, pixelWidth, lst, l, r):
    if l < r:
        piv = partition(Surface, screenWidth, pixelWidth, lst, l, r)
        quick_sort(Surface, screenWidth, pixelWidth,lst, l, piv - 1)
        quick_sort(Surface, screenWidth, pixelWidth,lst, piv + 1, r)


def partition(Surface, screenWidth, pixelWidth, lst, l, r):
    i = l
    j = r - 1
    pivot = lst[r][2]

    while i < j:
        while i < r and lst[i][2] < pivot:
            i = i + 1
        while j > l and lst[j][2] >= pivot:
            j = j - 1
        if i < j:
            VisCom.swap(Surface, screenWidth, pixelWidth, lst, i, j)
            pygame.time.delay(delay)
            pygame.display.update()
    if lst[i][2] > pivot:
        VisCom.swap(Surface, screenWidth, pixelWidth,lst, i, r)
    pygame.time.delay(delay)
    pygame.display.update()
    return i


