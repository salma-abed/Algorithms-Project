# Algorithms-Project
import pygame
import time
from collections import deque
from queue import PriorityQueue
def setMaze():
    global maze
    maze = [
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
     [0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0],
     [0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,0],
     [0,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,0],
     [0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0],
     [0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0],
     [0,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0],
     [0,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0],
     [0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1,0],
     [0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0],
     [0,1,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0],
     [0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1,0,1,0],
     [0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0],
     [0,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0],
     [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
    ]
    global mazeRealCost
    mazeRealCost =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 155, 37, 101, 27, 104, 16, 115, 0, 99, 0, 33, 0, 76, 46, 44, 23, 95, 17, 185, 155, 120, 188, 73, 0, 200, 44, 108, 0, 31, 94, 25, 15, 53, 0, 75, 0],
     [0, 144, 0, 0, 0, 0, 0, 0, 0, 94, 0, 125, 0, 0, 0, 9, 0, 66, 0, 0, 0, 192, 0, 0, 0, 81, 0, 0, 0, 0, 0, 0, 0, 7, 0, 172, 0], 
     [0, 46, 96, 179, 85, 53, 5, 14, 0, 20, 145, 0, 138, 187, 2, 186, 0, 62, 0, 102, 71, 13, 4, 7, 0, 63, 10, 197, 18, 80, 0, 59, 0, 77, 169, 67, 0],
     [0, 0, 0, 0, 0, 28, 0, 0, 0, 0, 0, 67, 0, 0, 0, 92, 0, 155, 0, 137, 0, 62, 0, 0, 0, 19, 0, 0, 0, 0, 0, 149, 0, 56, 0, 0, 0], 
     [0, 3, 36, 77, 0, 66, 0, 79, 0, 4, 0, 14, 191, 160, 0, 46, 0, 192, 0, 27, 0, 167, 189, 0, 0, 95, 0, 197, 137, 110, 0, 183, 0, 46, 30, 152, 0], 
     [0, 96, 0, 0, 0, 28, 0, 126, 0, 51, 0, 121, 0, 0, 0, 36, 0, 0, 0, 0, 0, 159, 0, 0, 0, 156, 0, 69, 0, 0, 0, 172, 0, 0, 0, 123, 0], 
     [0, 164, 57, 27, 79, 108, 41, 129, 0, 138, 170, 55, 85, 37, 0, 158, 33, 10, 0, 193, 191, 178, 0, 82, 147, 19, 193, 198, 0, 1, 0, 117, 0, 105, 195, 154, 0], 
     [0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 190, 0, 0, 0, 0, 0, 0, 0, 175, 0, 0, 0, 182, 0, 0, 0, 110, 0, 128, 0, 120, 0, 135, 0], 
     [0, 119, 164, 78, 63, 79, 28, 93, 29, 57, 70, 126, 60, 92, 0, 37, 24, 193, 80, 72, 29, 34, 0, 33, 0, 176, 47, 110, 0, 95, 191, 59, 94, 43, 0, 180, 0], 
     [0, 3, 0, 97, 0, 0, 0, 0, 0, 69, 0, 32, 0, 0, 0, 17, 0, 148, 0, 137, 0, 0, 0, 61, 0, 78, 0, 0, 0, 168, 0, 0, 0, 74, 0, 90, 0], 
     [0, 29, 0, 2, 0, 109, 60, 48, 161, 80, 0, 109, 0, 150, 0, 26, 0, 109, 0, 133, 8, 95, 100, 175, 0, 19, 27, 171, 0, 129, 0, 43, 0, 164, 0, 53, 0],
     [0, 80, 0, 57, 0, 183, 0, 0, 0, 0, 0, 0, 0, 155, 0, 95, 0, 0, 0, 0, 0, 0, 0, 0, 0, 157, 0, 0, 0, 173, 0, 5, 0, 0, 0, 119, 0], 
     [0, 44, 0, 179, 0, 161, 0, 125, 169, 39, 103, 105, 0, 197, 97, 124, 0, 151, 6, 15, 56, 103, 0, 45, 5, 8, 131, 47, 0, 76, 82, 60, 0, 64, 138, 93, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
     ]
#VARIABLES
square = 25
maplimit = 35
setMaze()
(width, height) = (len(maze) * square, len(maze[0]) * square)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()
Solu_1 = {}
startx = 0
starty = 0 
endx = 0
endy = 0
path = []
explored = [] 
frontier = []
running =True

def wall(i,j):
    pygame.draw.rect(screen,(0,0,255),(j*square,i*square,square,square))
def food(i,j):
    pygame.draw.circle(screen,(255,255,255),(j*square+square//2, i * square+square//2),square//4)
def pacPath(i,j):
    pygame.draw.rect(screen,(0,0,0),(j*square,i*square,square,square))
def pacman(i,j):
    pygame.draw.circle(screen, (255,255,0),(j*square+square//2, i * square+square//2),square//4)
def greenTrack(i,j):
    pygame.draw.rect(screen,(0,255,0),(j*square,i*square,square,square))
def redTrack(i,j):
    pygame.draw.rect(screen,(255,0,0),(j*square,i*square,square,square))
def renderBoard():
    global startx, starty,endx, endy
    screen.fill((0,0,0))
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            element = maze[i][j]
            if element == 0:
                wall(i,j)
            elif element == 4:
                path.append((j,i))
                endx = j
                endy = i
                food(i,j)
            elif element == 1:
                    pacPath(i,j)
                    path.append((j,i))
            elif element == 3:
                startx = j
                starty = i
                pacman(i,j)
            elif element == 9:
                path.append((j,i))
                greenTrack(i,j)
            elif element == 10:
                path.append((j,i))
                redTrack(i,j)
    pygame.display.update()
def move(x,y):
    maze[y][x] = 10


def DFS(x,y):
    frontier.append((x,y))
    Solu_1[x,y] = x,y
    while len(frontier) > 0:
        time.sleep(0)
        current = (x,y)
        if (x - 1,y) in path and (x - 1,y) not in explored:
            left = (x - 1,y)
            Solu_1[left] = x,y
            frontier.append(left)
        if (x,y + 1) in path and (x,y + 1) not in explored:
            down = (x,y+1)
            Solu_1[down] = x,y
            frontier.append(down)
        if (x + 1,y) in path and (x+1,y) not in explored:
            right = (x + 1,y)
            Solu_1[right] = x,y
            frontier.append(right)
        if (x,y-1) in path and (x,y-1) not in explored:
            up = (x,y-1)
            Solu_1[up] = x,y
            frontier.append(up)
        x,y = frontier.pop()
        maze[y][x] = 9
        explored.append(current)
        if (x,y) == (endx,endy):
            return
        renderBoard()



def backRoute(x,y):
    global cost
    global score
    while(x,y) != (startx,starty):
        x,y = Solu_1[x,y]
        score+=mazeRealCost[x][y]
        move(x,y)
        time.sleep(0)
        renderBoard()
        cost += 1


    

    #Remove the comment of desired algo

renderBoard()

#DFS(startx,starty)

setMaze()
renderBoard()
cost = 0
score=0
backRoute(endx,endy)
print(cost)
print(score)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False