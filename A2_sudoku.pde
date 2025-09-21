// A2 Sudoku 9x9 Puzzle
int table[][] = new int[9][9];

void setup() {
  size(750, 750);  
  background(255);
  
  generateSudoku();
  makePuzzle(36);  // ทำโจทย์ (เว้นช่อง)
  
  drawGrid();
}

void drawGrid() {
  int cell = width / 9;  // คำนวณ cell อัตโนมัติ
  
  // วาดกรอบ
  for (int i = 0; i <= 9; i++) {
    if (i == 0 || i == 9) {
      strokeWeight(6);
    } else if (i % 3 == 0) {
      strokeWeight(3);
    } else {
      strokeWeight(1);  
    }
    line(i*cell, 0, i*cell, height);
    line(0, i*cell, width, i*cell);
  }
  
  // วาดตัวเลข
  textAlign(CENTER, CENTER);
  textSize(cell * 0.5);  // ปรับขนาด font ตาม cell
  fill(0);
  for (int r = 0; r < 9; r++) {
    for (int c = 0; c < 9; c++) {
      if (table[r][c] != 0) {
        text(table[r][c], c*cell + cell/2, r*cell + cell/2);
      }
    }
  }
}

// generate Sudoku แบบเต็ม
void generateSudoku() {
  solve(0, 0);
}

boolean solve(int row, int col) {
  if (row == 9) return true;
  int nextRow = (col == 8) ? row+1 : row;
  int nextCol = (col == 8) ? 0 : col+1;
  
  int[] nums = {1,2,3,4,5,6,7,8,9};
  shuffle(nums);
  
  for (int n : nums) {
    if (isSafe(row, col, n)) {
      table[row][col] = n;
      if (solve(nextRow, nextCol)) return true;
      table[row][col] = 0;
    }
  }
  return false;
}

boolean isSafe(int row, int col, int n) {
  for (int c = 0; c < 9; c++) if (table[row][c] == n) return false;
  for (int r = 0; r < 9; r++) if (table[r][col] == n) return false;
  int startRow = (row/3)*3, startCol = (col/3)*3;
  for (int r=startRow; r<startRow+3; r++) {
    for (int c=startCol; c<startCol+3; c++) {
      if (table[r][c] == n) return false;
    }
  }
  return true;
}

void shuffle(int[] arr) {
  for (int i=arr.length-1; i>0; i--) {
    int j = int(random(i+1));
    int tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
  }
}

void makePuzzle(int emptyCount) {
  int removed = 0;
  while (removed < emptyCount) {
    int r = int(random(9));
    int c = int(random(9));
    if (table[r][c] != 0) {
      table[r][c] = 0;
      removed++;
    }
  }
}
