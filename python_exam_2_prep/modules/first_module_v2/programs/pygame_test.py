import pygame

# Program will run as long as run variable equals True
run = True

# Window size
width = 400
height = 100

# Initialize pygame environment
pygame.init()

# Prepare window size
screen = pygame.display.set_mode((width, height))

# Make a font object of default font size 48
font = pygame.font.SysFont(None, 48)

# Make a text object representing the text provided,
# anti-aliasing = true, and white color (255,255,255)
text = font.render("Welcome to pygame", True, (255, 255, 255))

# insert the text into the (currently invisible) screen buffer
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))

# flip the screen buffers to make the text visible
pygame.display.flip()

while run:
    # get a list of all pending pygame events
    for event in pygame.event.get():
        # check whether the user has closed the window or
        # clicked somewhere inside it or pressed any key
        if event.type == pygame.QUIT\
        or event.type == pygame.MOUSEBUTTONUP\
        or event.type == pygame.KEYUP:
            # if so, stop executing code
            run = False