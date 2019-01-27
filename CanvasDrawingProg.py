import pygame
 
# Define some colors
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
MAROON = (128, 0, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)
FUCHSIA = (255, 0, 255)
GREEN = (0, 128, 0)
LIME = (0, 255, 0)
OLIVE = (128, 128, 0)
YELLOW = (255, 255, 0)
NAVY = (0, 0, 128)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)
CYAN = (0, 255, 255)

#Set Width and Height of each grid location
width = 45
height = 45

#Set Margin between cells
margin = 10

# Screen Zone constraints
CanvasPos = ((margin + width) * 8, (margin + height) * 8)
PalettePos = (600 - ((margin + width) * 2), (margin + height) * 8)
ResetPos = (349, 539, 349 + 85, 539 + 34)
              
# --- Screen-clearing code goes here
CANVAS = [[BLACK]*8 for _ in range(8)]
    
PALETTE = [[BLACK]*8 for _ in range(2)]
PALETTE [0][0] = BLACK
PALETTE [0][1] = GRAY
PALETTE [0][2] = MAROON
PALETTE [0][3] = PURPLE
PALETTE [0][4] = GREEN
PALETTE [0][5] = OLIVE
PALETTE [0][6] = NAVY
PALETTE [0][7] = TEAL
PALETTE [1][0] = SILVER
PALETTE [1][1] = WHITE
PALETTE [1][2] = RED
PALETTE [1][3] = FUCHSIA
PALETTE [1][4] = LIME
PALETTE [1][5] = YELLOW
PALETTE [1][6] = BLUE
PALETTE [1][7] = CYAN

PaintBrush = BLUE
    
pygame.font.init()
myfont = pygame.font.SysFont('Times New Roman MS', 45)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (600, 600)
screen = pygame.display.set_mode(size)

ResetSurface = myfont.render('Reset', False, (255, 255, 255), (255, 165, 0))
RedSurface = myfont.render('Red = ', False, (0, 0, 0))
BlueSurface = myfont.render('Blue = ', False, (0, 0, 0))
GreenSurface = myfont.render('Green = ', False, (0, 0, 0))
 
pygame.display.set_caption("Canvas")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Init screen
screen.fill(WHITE)
 
    # --- Drawing code should go here
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            if pos[0] < CanvasPos[0] and pos[1] < CanvasPos[1]:
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (width + margin)
                row = pos[1] // (height + margin)
                # Set that location to one
                CANVAS[column][row] = PaintBrush
                print("Click ", pos, "Grid coordinates: ", row, column, CanvasPos)
            elif pos[0] > PalettePos[0] and pos [1] < PalettePos[1]:
                column = (pos[0] - 490) // (width + margin)
                row = pos[1] // (height + margin)
                # Set paintbrush color from palette
                PaintBrush = PALETTE[column][row]
                print("Click ", pos, "Pal. coordinates: ", row, column, PalettePos)
            elif pos[0] > ResetPos[0] and\
            pos[0] < ResetPos[2] and\
            pos[1] > ResetPos[1] and\
            pos[1] < ResetPos[3]:
                CANVAS = [[BLACK]*8 for _ in range(8)]
                print("Click ", pos, "Grid coordinates: ", row, column, CanvasPos)
            else:
                
                # Set the screen background
                screen.fill(WHITE)
    
    # --- Draw Canvas ---
    for row in range(8):
        for column in range(8):
            pygame.draw.rect(screen,
                             BLACK,
                             [(margin + width) * column + (margin - 1),
                              (margin + height) * row + (margin - 1),
                              width + 2,
                              height + 2])
            pygame.draw.rect(screen,
                             CANVAS [column][row],
                             [(margin + width) * column + margin,
                              (margin + height) * row + margin,
                              width,
                              height])           
    # --- Draw pallet for color choices ---
    for row in range(8):
        for column in range(2):
            pygame.draw.rect(screen,
                             BLACK,
                             [(margin + width) * column + (margin - 1) + 480,
                              (margin + height) * row + (margin - 1),
                              width + 2,
                              height + 2])
            pygame.draw.rect(screen,
                             PALETTE [column][row],
                             [(margin + width) * column + margin + 480,
                              (margin + height) * row + margin,
                              width,
                              height])
    # --- Draw paint brush display
    pygame.draw.rect(screen, BLACK, [479 + margin, 479, 102, 102])
    pygame.draw.rect(screen, PaintBrush, [480 + margin, 480, 100, 100])

    # --- Draw a Reset button and RGB Values
    R,G,B = PaintBrush
    RedSurface = myfont.render('Red = ' + str(R), False, (0, 0, 0), (255, 255, 255))
    GreenSurface = myfont.render('Green = ' + str(G), False, (0, 0, 0), (255, 255, 255))
    BlueSurface = myfont.render('Blue = ' + str(B), False, (0, 0, 0), (255, 255, 255))
    pygame.draw.rect(screen, WHITE, [149, ((height + margin) * 8) + 29,
                                     340, ((height + margin) * 8) + 160])
    screen.blit(RedSurface, (150, ((height + margin) * 8) + 30))
    screen.blit(GreenSurface, (150, ((height + margin) * 8) + 70))
    screen.blit(BlueSurface, (150, ((height + margin) * 8) + 110))

    pygame.draw.rect(screen, BLACK, [349, 539, 85, 33])
    screen.blit(ResetSurface,(350, 540))    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
