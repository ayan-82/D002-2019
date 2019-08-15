# Tic-Tac-Toe

def printcell(cells):
    print("-" * 13)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 13)


def check_col(cells):
    for i in range(0, 2):
        if cells[0][i] == cells[1][i] == cells[2][i] != ' ':
            return True
    return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False


    

cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]

printcell(cells)
p = 0
game = True
while game:
    col = int(input("Please enter column\n"))
    row = int(input("Please enter row\n"))
    if cells[row][col] == ' ':
        if p%2 == 0:
          sym  = 'X'
        else:
          sym = 'O'
        cells[row][col] = sym
        printcell(cells)
        p = p+1
    else:
         print("It is taken already")
        

        
    for x in range (0,3): 
      if (cells[x][0] == cells[x][1] == cells[x][2] == sym) or (cells[0][x] == cells[1][x] == cells[2][x] == sym) or (cells[0][0] == cells[1][1] == cells[2][2] == sym) or (cells[2][0] == cells[1][1] == cells[0][2] == sym):
        print(sym, "wins!")
        break
        game = False
        

    if not ' ' in cells[0] and not ' ' in cells[1] and not ' ' in cells[2] :
        print('Draw')
        game = False
     

    


