from graphics import *
import random
def bfs(win,source,target):
    visited = []
    for i in range(rows):
        add = []
        for j in range(columns):
            add.append(False)
        visited.append(add)
    si,sj = source[0],source[1]
    ti,tj = target[0],target[1]
    visited[si][sj] = True
    fifo = []
    fifo.append([si,sj,[]])
    while len(fifo) != 0:
        node = fifo.pop(0)
        si = node[0]
        sj = node[1]
        if si == ti and sj == tj:
            return path
        path = node[2]
        if si + 1 in range(rows) and not visited[si+1][sj]:
            if si + 1 == ti and sj == tj:
                return path
            fifo.append([si+1,sj,path + [[si+1,sj]]])
            visited[si+1][sj] = True
            square = Rectangle(Point(sj*cd,(si+1)*rd),Point(cd*(sj+1),rd*(si+2)))
            square.setFill("orange")
            square.draw(win)
            update(time)
        if si - 1 in range(rows) and not visited[si-1][sj]:
            if si - 1 == ti and sj == tj:
                return path
            fifo.append([si-1,sj,path + [[si-1,sj]]])
            visited[si-1][sj] = True
            square = Rectangle(Point(sj*cd,(si-1)*rd),Point(cd*(sj+1),rd*si))
            square.setFill("orange")
            square.draw(win)
            update(time)
        if sj + 1 in range(columns) and not visited[si][sj+1]:
            if si == ti and sj + 1 == tj:
                return path
            fifo.append([si,sj+1,path + [[si,sj+1]]])
            visited[si][sj+1] = True
            square = Rectangle(Point((sj+1)*cd,si*rd),Point(cd*(sj+2),rd*(si+1)))
            square.setFill("orange")
            square.draw(win)
            update(time)
        if sj - 1 in range(columns) and not visited[si][sj-1]:
            if si == ti and sj - 1 == tj:
                return path
            fifo.append([si,sj-1,path + [[si,sj-1]]])
            visited[si][sj-1] = True
            square = Rectangle(Point((sj-1)*cd,si*rd),Point(cd*(sj),rd*(si+1)))
            square.setFill("orange")
            square.draw(win)
            update(time)
    return []
def dfs(win,source,target):
    visited = []
    for i in range(rows):
        add = []
        for j in range(columns):
            add.append(False)
        visited.append(add)
    si,sj = source[0],source[1]
    ti,tj = target[0],target[1]
    visited[si][sj] = True
    fifo = []
    fifo.append([si,sj,[]])
    while len(fifo) != 0:
        node = fifo.pop()
        si = node[0]
        sj = node[1]
        if si == ti and sj == tj:
            return path
        path = node[2]
        if si + 1 in range(rows) and not visited[si+1][sj]:
            if si + 1 == ti and sj == tj:
                return path
            fifo.append([si+1,sj,path + [[si+1,sj]]])
            visited[si+1][sj] = True
            square = Rectangle(Point(sj*cd,(si+1)*rd),Point(cd*(sj+1),rd*(si+2)))
            square.setFill("orange")
            square.draw(win)
            update(time)
        if si - 1 in range(rows) and not visited[si-1][sj]:
            if si - 1 == ti and sj == tj:
                return path
            fifo.append([si-1,sj,path + [[si-1,sj]]])
            visited[si-1][sj] = True
            square = Rectangle(Point(sj*cd,(si-1)*rd),Point(cd*(sj+1),rd*si))
            square.setFill("orange")
            square.draw(win)
            update(time)
        if sj + 1 in range(columns) and not visited[si][sj+1]:
            if si == ti and sj + 1 == tj:
                return path
            fifo.append([si,sj+1,path + [[si,sj+1]]])
            visited[si][sj+1] = True
            square = Rectangle(Point((sj+1)*cd,si*rd),Point(cd*(sj+2),rd*(si+1)))
            square.setFill("orange")
            square.draw(win)
            update(time)
        if sj - 1 in range(columns) and not visited[si][sj-1]:
            if si == ti and sj - 1 == tj:
                return path
            fifo.append([si,sj-1,path + [[si,sj-1]]])
            visited[si][sj-1] = True
            square = Rectangle(Point((sj-1)*cd,si*rd),Point(cd*(sj),rd*(si+1)))
            square.setFill("orange")
            square.draw(win)
            update(time)
    return []
def setup():
    global win, grid
    win = GraphWin("Pathfinding", 800, 800)
    win.setBackground("blue")
def draw():
    y = 0
    for i in range(len(grid)):
        x = 0
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                square = Rectangle(Point(x,y),Point(x+800//columns,y+800//rows))
                square.setFill("blue")
                square.draw(win)

            else:  
                square = Rectangle(Point(x,y),Point(x+800//columns,y+800//rows))
                square.setFill("green")
                square.draw(win)
            x += 800//columns
        y += 800//rows
time = 10
grid = []
for i in range(8):
    row = [0] * 6
    grid.append(row)
sx,sy = 0,5
tx,ty = 3,4
grid[sx][sy] = 1
grid[tx][ty] = 1
rows = len(grid)
columns = len(grid[0])
cd = 800//columns
rd = 800//rows
setup()
draw()
while True:
    algo = input("dfs or bfs")
    draw()
    if algo == "bfs":
        path = bfs(win,[sx,sy],[tx,ty])
        for coord in path:
            x = coord[0]
            y = coord[1]
            square = Rectangle(Point(y*cd,x*rd),Point(cd*(y+1),rd*(x+1)))
            square.setFill("yellow")
            square.draw(win)
            update(time)
    if algo == "dfs":
        path = dfs(win,[sx,sy],[tx,ty])
        for coord in path:
            x = coord[0]
            y = coord[1]
            square = Rectangle(Point(y*cd,x*rd),Point(cd*(y+1),rd*(x+1)))
            square.setFill("yellow")
            square.draw(win)
            update(time)
