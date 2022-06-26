"""
Brute Force Sudoku Solver
In Sudoku the board is  9x9 grid of squares. There are 9 rows and 9 columns. There are 9 boxes which are 3x3 in size. rows columns and boxes are all units, so there are 27 units. To win the game the board has to be filled in a such a way so that no unit contains a duplicate number
"""

import Board
def filter2(fn, lis):
    tempList = []
    for i in lis:
        if fn(i):
            tempList.append(i)
    return tempList

def solved(bd):
    return not (False in bd)

def find_blank(bd):
    if (bd[0] == False):
        return 0
    else:
        return 1+ find_blank(bd[1::])

def fill_cell(bd,pos):
    tempList =[]
    tempBd = bd
    for i in range(1,10):
        tempBd[pos]=i
        tempList.append(list(tempBd))
    return tempList

def solve_bd (bd):
    if solved(bd):
       return bd
    else:
        return solve_lobd(next_board(bd))


def keep_only_val(unit):
    return filter2(lambda a: not False == a, unit)

# print(keep_only_val(Board.BD2))

def valid_board(bd) -> bool:
    bdUnit = []
    for i in Board.listUnit:
        for z in i:
            bdUnit.append(bd[z])
        bdUnit=keep_only_val(bdUnit)
        if (len(bdUnit)==len(set(bdUnit))):
            bdUnit=[]
        else:
            return False
    return True
        
print(valid_board(Board.BD2),)    


def solve_lobd (lobd):
    if lobd == []:
        return False
    else:
        result = solve_bd(lobd[0])
        if (result == (not False)):
            return result
        else:
            return solve_lobd(lobd[1::])



def solve (bd) -> Board:
    """
    Solves the sudoku board and returns the solved board

    
    """
    return solve_bd(bd)

def next_board(bd):
    """
    Generates the next board from a given board
    """
    return filter2(valid_board, fill_cell(bd, find_blank(bd)))

print(next_board(Board.BD2))




# print(fill_cell(Board.BD2,find_blank(Board.BD2)))

    


# print(solve(Board.BD2))

