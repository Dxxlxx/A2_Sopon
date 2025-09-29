import random

grid = [[0 for _ in range(9)] for _ in range(9)]
cell = 60
selected = None
button_y = 560
locked = [[False for _ in range(9)] for _ in range(9)]

def setup():
    size(540, 620)
    textAlign(CENTER, CENTER)
    textSize(24)
    makePuzzle(removals=10)  

def draw():
    background(255)
    drawGrid()
    drawNumbers()
    drawButtons()

def drawGrid():
    for i in range(10):
        strokeWeight(3 if i % 3 == 0 else 1)
        line(0, i*cell, 9*cell, i*cell)
        line(i*cell, 0, i*cell, 9*cell)
    if selected:
        r, c = selected
        noFill()
        strokeWeight(3)
        rect(c*cell, r*cell, cell, cell)

def drawNumbers():
    textSize(32)
    for r in range(9):
        for c in range(9):
            if grid[r][c] != 0:
                fill(0)
                text(str(grid[r][c]), c*cell + cell/2, r*cell + cell/2)

def drawButtons():
    textSize(20)
    for i in range(9):
        x = i * 60
        y = button_y
        fill(200)
        rect(x, y, 60, 50)
        fill(0)
        text(str(i+1), x+30, y+25)
    fill(255, 180, 180)

def mousePressed():
    global selected
    if mouseY < 540:
        c = mouseX // cell
        r = mouseY // cell
        if 0 <= r < 9 and 0 <= c < 9:
            selected = (r, c)
    elif button_y <= mouseY <= button_y+50:
        i = mouseX // 60
        if 0 <= i < 9 and selected:
            r, c = selected
            if not locked[r][c]:
                if isValid(r, c, i+1):
                    grid[r][c] = i+1

def fillGrid():
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                nums = list(range(1, 10))
                random.shuffle(nums)
                for num in nums:
                    if isValid(i, j, num):
                        grid[i][j] = num
                        if fillGrid():
                            return True
                        grid[i][j] = 0
                return False
    return True

def makePuzzle(removals=40):
    for r in range(9):
        for c in range(9):
            grid[r][c] = 0
            locked[r][c] = False
    fillGrid()
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)
    count = 0
    for r, c in cells:
        if count >= removals:
            break
        grid[r][c] = 0
        locked[r][c] = False
        count += 1
    for r in range(9):
        for c in range(9):
            if grid[r][c] != 0:
                locked[r][c] = True

def isValid(row, col, val):
    for c in range(9):
        if grid[row][c] == val:
            return False
    for r in range(9):
        if grid[r][col] == val:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for r in range(startRow, startRow+3):
        for c in range(startCol, startCol+3):
            if grid[r][c] == val:
                return False
    return True
