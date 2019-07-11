# import pygame library so we can use it!
import pygame

# run initialization code on the library
pygame.init()

# setup display dimensions
display_width = 1000
display_height = 800

gameSurface = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Window Caption!')

# setup game resources
# color definitions
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (240, 240, 240)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

# variables
mouseX = 0
mouseY = 0
pMouseX = 0
pMouseY = 0
size = 10
colorArray = [RED, GREEN, BLUE, WHITE]
colorNum = 0

# set background before we draw
gameSurface.fill(WHITE)

# main game loop
running = True  # when running is True game loop will run
while running == True:

    # fill entire screen (clear background)
    # gameSurface.fill(255)

    # get input events and respond to them
    # if event is .QUIT
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False

        # handle input events
        elif event.type == pygame.KEYDOWN:
            # clear screen
            if event.key == pygame.K_SPACE:
                gameSurface.fill(WHITE)
            # change colors
            if event.key == pygame.K_1:
                colorNum = 0
            if event.key == pygame.K_2:
                colorNum = 1
            if event.key == pygame.K_3:
                colorNum = 2
            if event.key == pygame.K_0:
                colorNum = 3
            # change size of circles
            if event.key == pygame.K_MINUS:
                size -= 1
                if size < 1:
                    size = 1
            if event.key == pygame.K_EQUALS:  # really the + key without shift
                size += 1

    # print(pygame.mouse.get_pos())  #print mouse position to console

    # this needs to constantly update so move out of mouse if statement
    pmouseX, pmouseY = pygame.mouse.get_rel()
    mouseX, mouseY = pygame.mouse.get_pos()

    # use state checking to determine if mouse is pressed every frame
    # if the right button is pressed
    if pygame.mouse.get_pressed() == (1, 0, 0):


        # pygame.draw.circle(gameSurface, colorArray[arrayPosition], (mouseX, mouseY), size)
        # pmouseX,pmouseY = pygame.mouse.get_rel()  # this needs to constantly update so move out of mouse if statement
        pygame.draw.line(gameSurface, colorArray[colorNum], (mouseX - pmouseX, mouseY - pmouseY), (mouseX, mouseY),
                         size)
        print("pmouseX= " + pmouseX.__str__)
    # pygame.draw.circle(gameSurface, colorArray[arrayPosition], (mouseX, mouseY), size)
    # if the right button is pressed
    if pygame.mouse.get_pressed() == (0, 0, 1):
        pygame.draw.circle(gameSurface, colorArray[colorNum], (mouseX, mouseY), size)

    # update and redraw entire screen
    pygame.display.flip()
    # update some of the screen
    # pygame.display.update()
