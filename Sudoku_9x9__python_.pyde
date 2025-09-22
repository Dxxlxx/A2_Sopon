#A2_Sudoku python Sopon
import random
table = [
 [0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0]
]

def setup():
    size(900, 900)
    background(255)
    
    generateSudoku()
    makePuzzle(40)
    drawGrid()

def drawGrid():
    cell = width // 9
    for i in range(10):
        if i == 0 or i == 9:
            strokeWeight(6)
        elif i % 3 == 0:
            strokeWeight(3)
        else:
            strokeWeight(1)
        line(i * cell, 0, i * cell, height)
        line(0, i * cell, width, i * cell)
    
    textAlign(CENTER, CENTER)
    textSize(cell * 0.6)
    fill(0)
    for r in range(9):
        for c in range(9):
            if table[r][c] != 0:
                text(str(table[r][c]), c * cell + cell // 2, r * cell + cell // 2)

def generateSudoku():
    solve(0, 0)

def solve(row, col):
    if row == 9:
        return True

    if col == 8:
        nextRow = row + 1
        nextCol = 0
    else:
        nextRow = row
        nextCol = col + 1

    nums = [1,2,3,4,5,6,7,8,9]
    shuffle(nums)
    for n in nums:
        if isSafe(row, col, n):
            table[row][col] = n
            if solve(nextRow, nextCol):
                return True
            table[row][col] = 0
    return False

def isSafe(row, col, n):
    for c in range(9):
        if table[row][c] == n:
            return False
    for r in range(9):
        if table[r][col] == n:
            return False
    
    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    for r in range(startRow, startRow + 3):
        for c in range(startCol, startCol + 3):
            if table[r][c] == n:
                return False
    return True

def shuffle(arr):
    for i in range(len(arr)-1, 0, -1):
        j = int(random.randint(0, i))
        arr[i], arr[j] = arr[j], arr[i]

def makePuzzle(emptyCount):
    removed = 0
    while removed < emptyCount:
        r = random.randint(0, 8)
        c = random.randint(0, 8)
        if table[r][c] != 0:
            table[r][c] = 0
            removed += 1
