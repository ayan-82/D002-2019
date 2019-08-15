def printcell(cells):
    print("-" * 25)
    for i in range(0, 6):
        for j in range(0, 6):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 25)


def checker1(col,row,num):
        for i in range (0,6):
          if num == cells[i][col] or num == cells[row][i] or cells[row][col] != ' ':
            return False
            break
        return True
          
         

def checker2(col,row,num):
        if row%2 == 0:
            q = row +1
        else:
            q = row -1
        if 0<= col <= 2:
            x = 0
            y =3
        else:
            x = 3
            y =6
        for i in range (x,y):
          if num == cells[q][i]:
            return False
            break
        return True
        
          
        

    

cells = [[' ',' ','3',' ','1',' '], ['5','6',' ','3','2',' '], [' ','5','4','2',' ','3'], ['2',' ','6','4','5',' '], [' ','1','2',' ','4','5'], [' ','4',' ','1',' ',' ']]
printcell(cells)
game = True
while game:
    row = int(input("Please enter row\n"))
    col = int(input("Please enter column\n"))
    num = input("Please enter a number\n")  
    if checker1(col,row,num) == checker2(col,row,num) == True:
            cells[row][col] = num
            printcell(cells)

    if not ' ' in cells[0] and not ' ' in cells[1] and not ' ' in cells[2] and not ' ' in cells[3] and not ' ' in cells[4] and not ' ' in cells[5] :
               game = False
               print ("Done!")

