import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Hill Climbing Path Finding Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.total_rows = total_rows
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
    
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED
    
    def make_open(self):
        self.color = GREEN
    
    def make_barrier(self):
        self.color= BLACK

    def make_start(self):
        self.color = ORANGE
    
    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self,win):
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))

    def update_neighbors(self,grid):
        self.neighbors= []
        if self.row+1 < self.total_rows and not grid[self.row+1][self.col].is_barrier():
            self.neighbors.append(grid[self.row+1][self.col])

        if self.col+1 < self.total_rows and not grid[self.row][self.col+1].is_barrier():
            self.neighbors.append(grid[self.row][self.col+1])

        if self.row-1 >= 0 and not grid[self.row-1][self.col].is_barrier():
            self.neighbors.append(grid[self.row-1][self.col])

        if self.col-1 >=0 and not grid[self.row][self.col-1].is_barrier():
            self.neighbors.append(grid[self.row][self.col-1])
    
    def __lt__(self,other):
        return False

def h(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1-x2) + abs(y1-y2)

def reconstruct_path(came_from,current,draw):
    while current in came_from:
        current=came_from[current]
        current.make_path()
        draw()

def algorithm(draw, grid, start, end):
    open_set = start
    came_from = {}
    h_score = {spot: float("inf") for row in grid for spot in row}
    h_score[start] = h(start.get_pos(), end.get_pos())
    
    for row in grid:   
        for spot in row:
            h_score[spot] = h(spot.get_pos(), end.get_pos())

    while open_set != end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set
        
        next_spot = None
        for neighbor in current.neighbors:
            temp_h_score = h_score[neighbor]
            if next_spot is None or temp_h_score < h_score[next_spot]:
                next_spot = neighbor
                came_from[neighbor] = current

        if next_spot is None:
            break
        
        open_set = next_spot
        open_set.make_open()

        draw()
        
        if current != start:
            current.make_closed()

    if open_set == end:
        reconstruct_path(came_from, end, draw)
        end.make_end()
        start.make_start()
        return True
    else:
        return False


def make_grid(rows,width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i,j,gap,rows)
            grid[i].append(spot)
    return grid

def draw_grid(win,rows,width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win,GREY,(0,i*gap),(width,i*gap))  # horizontal lines (start)(end)
        for j in range(rows):
            pygame.draw.line(win,GREY,(j*gap,0),(j*gap,width)) # vertical lines (start)(end)

def draw(win,grid,rows,width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win,rows,width)
    pygame.display.update()

def get_clicked_pos(pos,rows,width):
    gap = width // rows
    x,y = pos
    row = x // gap
    col = y // gap
    return row,col

def main(win,width):
    ROWS = 50
    grid = make_grid(ROWS,width)

    start = None
    end = None

    run = True

    while(run):
        draw(win,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:
                pos=pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos,ROWS,width)
                spot = grid[row][col]
                if not start and spot!=end:
                    start = spot
                    start.make_start()
                elif not end and spot!=start:
                    end=spot
                    end.make_end()
                elif spot!=start and spot!=end:
                    spot.make_barrier()
            elif pygame.mouse.get_pressed()[2]:
                pos=pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos,ROWS,width)
                spot = grid[row][col]
                spot.reset()
                if spot==start:
                    start=None
                elif spot==end:
                    end=None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    
                    algorithm(lambda:draw(win,grid,ROWS,width),grid,start,end)

                if event.key == pygame.K_c:
                    start=None
                    end=None
                    grid=make_grid(ROWS,width)
    pygame.quit()

main(WIN,WIDTH)