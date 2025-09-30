grid = []
cell = 60
selected = None
button_y = 560

def setup():
    global grid, locked
    size(540, 620)
    textAlign(CENTER, CENTER)
    textSize(24)
    
    lines = loadStrings("sudoku.txt")
    for line in lines:
        row = [int(x) for x in line.replace(',', ' ').split()]
        grid.append(row)

    locked = [[grid[r][c] != 0 for c in range(9)] for r in range(9)]


def draw():
    background(255)
    drawGrid()
    drawNumbers()
    drawButtons()
    Finish()

def drawGrid():
    i = 0
    while i < 10:
        strokeWeight(3 if i % 3 == 0 else 1)
        line(0, i * cell, 9 * cell, i * cell)
        line(i * cell, 0, i * cell, 9 * cell)
        i += 1

    if selected:
        r, c = selected
        noFill()
        strokeWeight(3)
        rect(c * cell, r * cell, cell, cell)

def drawNumbers():
    textSize(32)
    r = 0
    while r < 9:
        c = 0
        while c < 9:
            if grid[r][c] != 0:
                if locked[r][c]:
                    fill(0)
                elif isConflict(r, c, grid[r][c]):
                    fill(255, 0, 0)
                else:
                    fill(0, 200, 0)
                text(str(grid[r][c]), c * cell + cell/2, r * cell + cell/2)
            c += 1
        r += 1

def drawButtons():
    textSize(30)
    i = 0
    while i < 9:
        x = i * 60
        y = button_y
        fill(220)
        rect(x, y, 60, 60)
        fill(0)
        text(str(i + 1), x + 30, y + 30)
        i += 1

def mousePressed():
    global selected
    if mouseY < 540:
        c = mouseX // cell
        r = mouseY // cell
        if 0 <= r < 9 and 0 <= c < 9:
            selected = (r, c)
    elif button_y <= mouseY <= button_y + 50:
        i = mouseX // 60
        if 0 <= i < 9 and selected:
            r, c = selected
            if not locked[r][c]:
                grid[r][c] = i + 1

def isConflict(row, col, val):
    c = 0
    while c < 9:
        if c != col and grid[row][c] == val:
            return True
        c += 1
    r = 0
    while r < 9:
        if r != row and grid[r][col] == val:
            return True
        r += 1
    startRow = row - row % 3
    startCol = col - col % 3
    r = startRow
    while r < startRow + 3:
        c = startCol
        while c < startCol + 3:
            if (r != row or c != col) and grid[r][c] == val:
                return True
            c += 1
        r += 1
    return False

def Finish():
    r = 0
    while r < 9:
        c = 0
        while c < 9:
            if grid[r][c] == 0:
                return False
            if isConflict(r, c, grid[r][c]):
                return False
            c += 1
        r += 1

    background(255)
    fill(0)
    textSize(50)
    textAlign(CENTER, CENTER)
    text("You Win !", width / 2, height / 2)
    noLoop()
    return True
