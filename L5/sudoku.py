def printcell(cells):
    print("-" * 25)
    for i in range(0, 6):
        for j in range(0, 6):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 25)


def check_col(cells):
    for i in range(0, 5):
        if cells[0][i] == cells[1][i] == cells[2][i]  == cells[3][i] == cells[4][i] == cells[5][i] != ' ':
            return True
    return False

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return True
    return False


    

cells = [[' ',' ','3',' ','1',' '], ['5','6',' ','3','2',' '], [' ','5','4','2',' ','3'], ['2',' ','6','4','5',' '], [' ','1','2',' ','4','5'], [' ','4',' ','1',' ',' ']]
printcell(cells)

while True:
    col = int(input("Please enter column\n"))
    row = int(input("Please enter row\n"))
    num = input("Please enter a number")
    if cells[row][col] == ' ':
        cells[row][col] = num
        printcell(cells)
    else:
         print("It is taken already")
