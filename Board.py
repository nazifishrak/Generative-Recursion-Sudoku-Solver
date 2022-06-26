"""
Board is a flat list of 81 numbers which is represented like this
[
 1, 2, 3, 4, 5, 6, 7, 8, 9,
10,11,12,13,14,15,16,17,18,
19,20,21,22,23,24,25,26,27,
28,29,30,31,32,33,34,35,36,
37,38,39,40,41,42,43,44,45,
46,47,48,49,50,51,52,53,54,
55,56,57,58,59,60,61,62,63,
64,65,66,67,68,69,70,71,72,
73,74,75,76,77,78,79,80,81
]
"""


f = False
BD1 = [
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f
]

BD2 = [
 1, 2, 3, 4, 5, 6, 7, 8, 9,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f,
 f, f, f, f, f, f, f, f, f
]
BD3 = [
 1, f, f, f, f, f, f, f, f,
 2, f, f, f, f, f, f, f, f,
 3, f, f, f, f, f, f, f, f,
 4, f, f, f, f, f, f, f, f,
 5, f, f, f, f, f, f, f, f,
 6, f, f, f, f, f, f, f, f,
 7, f, f, f, f, f, f, f, f,
 8, f, f, f, f, f, f, f, f,
 9, f, f, f, f, f, f, f, f
]

boxes = [
    [0,1,2,9,10,11,18,19,20],
    [3,4,5,12,13,14,21,22,23],
    [6,7,8,15,16,17,24,25,26],
    [27,28,29,36,37,38,45,46,47],
    [30,31,32,39,40,41,78,49,50],
    [33,34,35,42,43,44,51,52,53],
    [54,55,56,63,64,65,72,73,74],
    [57,58,59,66,67,68,75,76,77],
    [60,61,62,69,70,71,78,79,80]
]

def rowsGenerator():
    '''
    ***HELPER METHOD***
    returns a list of all the rows in the sudoku board
    ''' 
    counter = 0;
    mainList =[]
    tempList =[]
    while(len(mainList)<9):
        
        while(len(tempList)<9):
            
            tempList.append(counter)
            counter= counter+1
        mainList.append(tempList)
        tempList = []    
    
    return mainList

def columnsGenerator():
    
    '''
    ***HELPER METHOD***
    returns a list of all the columns in the sudoku board
    ''' 

    mainList =[]
    tempList =[]
    for i in range(9):
        z=i
        while(len(tempList)<9):
            tempList.append(z)
            z = z + 9
        mainList.append(tempList)
        tempList = []
    return mainList


def generateUnits():
    """
    ***HELPER METHOD***
    returns a list of rows, columns and boxes in a  sudoku board
    """
    tempList = []
    for i in rowsGenerator():
        tempList.append(i)
    for i in columnsGenerator():
        tempList.append(i)
    for i in boxes:
        tempList.append(i)
    return tempList


def coordinateToPos(r,c):
    return r*9+c


listUnit = [[0, 1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32, 33, 34, 35], [36, 37, 38, 39, 40, 41, 42, 43, 44], [45, 46, 47, 48, 49, 50, 51, 52, 53], [54, 55, 56, 57, 58, 59, 60, 61, 62], [63, 64, 65, 66, 67, 68, 69, 70, 71], [72, 73, 74, 75, 76, 77, 78, 79, 80], [0, 9, 18, 27, 36, 45, 54, 63, 72], [1, 10, 19, 28, 37, 46, 55, 64, 73], [2, 11, 20, 29, 38, 47, 56, 65, 74], [3, 12, 21, 30, 39, 48, 57, 66, 75], [4, 13, 22, 31, 40, 49, 58, 67, 76], [5, 14, 23, 32, 41, 50, 59, 68, 77], [6, 15, 24, 33, 42, 51, 60, 69, 78], [7, 16, 25, 34, 43, 52, 61, 70, 79], [8, 17, 26, 35, 44, 53, 62, 71, 80], [0, 1, 2, 9, 10, 11, 18, 19, 20], [3, 4, 5, 12, 13, 14, 21, 22, 23], [6, 7, 8, 15, 16, 17, 24, 25, 26], [27, 28, 29, 36, 37, 38, 45, 46, 47], [30, 31, 32, 39, 40, 41, 78, 49, 50], [33, 34, 35, 42, 43, 44, 51, 52, 53], [54, 55, 56, 63, 64, 65, 72, 73, 74], [57, 58, 59, 66, 67, 68, 75, 76, 77], [60, 61, 62, 69, 70, 71, 78, 79, 80]]