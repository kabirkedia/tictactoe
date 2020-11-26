import pygame as pg
import sys
import time
from pygame.locals import *

#defining global variables

#x or o variables
XO='x'
#to determine if a person is a winner at any point
winner = None
#to determine if game is draw
draw = None
#height and width of the game window
height=400
width=400
#background color(WHITE)
back_color=(255,255,255)
#color of the lines(BLACK)
line_color=(0,0,0)
#setting up a 3*3 board on the canavas
board=[[None]*3,[None]*3,[None]*3]

#Designing the game window

#intiate game window
pg.init()
#setting fps manually
fps=60
#setting clock
CLOCK=pg.time.Clock()
#loading the window
screen=pg.display.set_mode((width,height+100),0,32)
#loading images as python object
init_window=pg.image.load("Cover.png")
X_image=pg.image.load("Ximage.png")
O_image=pg.image.load("Oimage.png")

#display the name of the init_window
display_caption=pg.display.set_caption("TIC TAC TOE")

#resizing images
init_window=pg.transform.scale(init_window,(width,height+100))
x_img=pg.transform.scale(X_image,(80,80))
o_img=pg.transform.scale(O_image,(80,80))

#function
def game_init_window():
#display screen

    screen.blit(init_window,(0,0))

    #updating the screen
    pg.display.update()
    time.sleep(3)
    screen.fill((255,255,255))

    #drawing horizontal lines
    pg.draw.line(screen, line_color , (width/3,0), (width/3,height),7)
    pg.draw.line(screen, line_color , (width/3*2,0), (width/3*2,height),7)

    #drawing vertical lines
    pg.draw.line(screen, line_color , (0,height/3), (width,height/3),7)
    pg.draw.line(screen, line_color , (0,height/3*2), (width,height/3*2),7)

    draw_status()

def draw_status():
    global draw
    #Determinig th status of th game

    if winner is None:
        message = XO.upper()+"'s Turn"
    else:
        message = winner.upper()+" is the winner"
    if draw:
        message = "It's a DRAW"

    #creating a font object

    font = pg.font.Font(None,30)

    #creating the text size and back_color
    text = font.render(message,1,(255,255,255))

    #creating a small block at the bottom for the message and copying the message

    screen.fill((0,0,0),(0,400,500,100))
    text_rect=text.get_rect(center=(width/2,450))
    screen.blit(text,text_rect)
    pg.display.update()


#MAIN ALGORITHM

def check_win():

    global board, winner ,draw

    #checking for row
    for row in range(0,3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None):
            winner = board[row][0]
            pg.draw.line(screen, (128,0,128),(0, (row+1)*height/3 - height/6) , (width, (row+1)*height/3 - height/6), 4)
            break
    #checking column
    for column in range(0,3):
        if (board[0][column] == board[1][column] == board[2][column]) and (board[0][column] is not None):
            winner = board[0][column]
            pg.draw.line(screen, (128,0,128),((column+1)*width/3 - width/6 ,0), ((column+1)*width/3 - width/6 , height), 4)
            break

    #checking diagonals
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        winner = board[0][0]
        pg.draw.line(screen ,(128,0,128), (50,50), (350,350), 4)


    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        winner = board[0][0]
        pg.draw.line(screen ,(128,0,128), (50,350), (350,50), 4)

    #checking if its a draw

    if (all([all(row) for row in board]) and winner is None):
        draw = True

    draw_status()

# getting the user input

def drawXO(row , col):
    global board, XO
#posx and posy to position the images of x and o
    if(row == 1):
        posx = 30
    elif(row == 2):
        posx = 30 + width/3
    elif(row == 3):
        posx = 30 + 2*width/3

    if(col == 1):
        posy = 30
    elif(col == 2):
        posy = 30 + height/3
    elif(col == 3):
        posy = 30 + 2*height/3
#setting up user display
    board[row-1][col-1] = XO
    if(XO == 'x'):
        screen.blit(x_img,(posy,posx))
        XO = 'o'
    else:
        screen.blit(o_img,(posy,posx))
        XO = 'x'
    pg.display.update()

def user_click():
    x,y=pg.mouse.get_pos()

    if(x<width/3):
        col=1
    elif(x<width / 3 * 2):
        col=2
    elif(x<width):
        col=3
    else:
        col=None

    if(y<height/3):
        row=1
    elif(y<height/3*2):
        row=2
    elif(y<height):
        row=3
    else:
        row=None

 
    if(row and col and board[row-1][col-1] is None):
        #drawing the images
        global XO
        drawXO(row,col)
        check_win()

#reset button

def reset_game():
    global draw,winner,draw,XO
    XO='x'
    winner=None
    draw=False
    time.sleep(2)
    game_init_window()
    pg.quit()
    pg.init()
    print("reset_game")
    board=[[None]*3,[None]*3,[None]*3]

game_init_window()

while True:
    for event in pg.event.get():
        if (event.type == QUIT):
            pg.quit()
            sys.exit()
        else:
            print("in event")
            user_click()
            if(winner or draw):
                reset_game()

    pg.display.update()
    CLOCK.tick(fps)
