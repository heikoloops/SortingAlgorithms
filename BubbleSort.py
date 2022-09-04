import pygame
import VisCom


width = 800
finished = False
number_of_pixels = 250 # total number of pixels in a row, the number of elements to sort is half of it
# the max number of pixels should be 400
pixel_width = int(width / number_of_pixels) # width of the lines




list_to_sort = [None for i in range(0,int(number_of_pixels/2))] # containts the start position of the line and the number which the line represents (x,y, factor)
delay = int(1/number_of_pixels * 1000)




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
    delay = int(1 / number_of_pixels * 10000)
    SCREEN = pygame.display.set_mode(size=(width, width))
def program_loop():
    global finished
    SCREEN.fill(VisCom.Colors.WHITE)
    VisCom.draw_lines(SCREEN, VisCom.Colors.BLACK, pixel_width, width, number_of_pixels, list_to_sort)
    pygame.display.update()
    sort_start = False
    counter =len(list_to_sort)
    finished = False
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                pygame.quit()
                #quit()
            if event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYDOWN:
                sort_start = True


        if counter > 1 and sort_start and not finished:
            for i in range(0, counter - 1):
                if list_to_sort[i][2] > list_to_sort[i + 1][2]:
                    VisCom.swap(SCREEN, width, pixel_width, list_to_sort, i, i + 1)
                #pygame.display.update() , slow visualization
                #clock.tick(60)
            pygame.time.delay(delay)
            pygame.display.update() # fast visualization

            counter -= 1
        if not finished:
            pygame.display.update()





