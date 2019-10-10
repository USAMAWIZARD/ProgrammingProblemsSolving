'''
I have wrote a program which can solve sudoko a puzzle
i have used a data frame as a sodoko bord
i have initialized all the prefilled boxes on the bord using filldefaultvalues  function
'''

import numpy as np
import pandas as pd

sudokobord= pd.DataFrame(index=[0,1,2,3,4,5,6,7,8], columns=[0,1,2,3,4,5,6,7,8])
canplaceonbord= pd.DataFrame(index=[0,1,2,3,4,5,6,7,8], columns=[0,1,2,3,4,5,6,7,8])
sudokobord=sudokobord.fillna(0)
caninsert=[]

def chkifzeroindataframe():
    for i in range(8):
        if 0 in sudokobord[i][:].values.tolist():
            return True
    return False
def getslicerepetations(x,y,i):
    list=getslice(x,y)
    #print(list)
    list=list.values.tolist()
    for  innerlist in list:
        if i in innerlist:
            return True
    return False
def getslice(x,y):
    if x>=0 and  x<=2 and y>=0 and  y<=2:
        return sudokobord.loc[[0,1,2],[0,1,2]]
    if x>=3 and x<=5 and y>=0 and  y<=2:
        return sudokobord.loc[[3, 4, 5], [0, 1, 2]]
    if x>=6 and x<=8 and y>=0 and  y<=2:
        return sudokobord.loc[[6, 7, 8], [0, 1, 2]]
    if x>=0 and x<=2 and y>=3 and  y<=5:
        return sudokobord.loc[[0, 1, 2], [3, 4, 5]]  #xy
    if x>=3 and x<=5 and y>=3 and  y<=5:
        return sudokobord.loc[[3, 4, 5], [3, 4, 5]]  #xy
    if x>=6 and x<=8 and y>=3 and  y<=5:
        return sudokobord.loc[[6, 7, 8], [3, 4, 5]]  #xy
    if x>=0 and x<=2 and y>=6 and  y<=8:
        return sudokobord.loc[[0, 1, 2], [6, 8, 7]]  #xy
    if x>=3 and x<=5 and y>=6 and  y<=8:
        return sudokobord.loc[[3, 4, 5], [6, 8, 7]]  #xy
    if x>=6 and x<=8 and y>=6 and  y<=8:
        return sudokobord.loc[[6, 7, 8], [6, 8, 7]]  #xy
def filldefaultvalues():
    global sudokobord
    sudokobord[0][0]=8
    sudokobord[2][0]=9
    sudokobord[6][0]=7
    sudokobord[8][0]=4
    sudokobord[1][1]=3
    sudokobord[7][1]=6
    sudokobord[0][2]=6
    sudokobord[2][2]=7
    sudokobord[3][2]=9
    sudokobord[5][2]=4
    sudokobord[6][2]=1
    sudokobord[8][2]=3
    sudokobord[2][3]=3
    sudokobord[3][3]=1
    sudokobord[5][3]=5
    sudokobord[6][3]=8
    sudokobord[2][5]=4
    sudokobord[3][5]=3
    sudokobord[5][5]=6
    sudokobord[6][5]=9
    sudokobord[0][6]=9
    sudokobord[2][6]=5
    sudokobord[3][6]=2
    sudokobord[5][6]=8
    sudokobord[6][6]=6
    sudokobord[8][6]=7
    sudokobord[1][7]=7
    sudokobord[7][7]=1
    sudokobord[0][8]=2
    sudokobord[2][8]=1
    sudokobord[6][8]=4
    sudokobord[8][8]=8
def whatCanIInsert(x,y):
    if sudokobord[x][y]:
        return False
    for i in range(1,10):
        if ((not(i in sudokobord.loc[y][:].values.tolist())) and (not(i in sudokobord.loc[:][x].values.tolist()) and (not(getslicerepetations(y,x,i))))):
            caninsert.append(i)
    return caninsert




filldefaultvalues()
while chkifzeroindataframe():
    for horizontal in range(0,9):
        for virtical in range(0,9):
            canplaceonbord[horizontal][virtical]=whatCanIInsert(horizontal,virtical)#xy
            caninsert=[]
    canplaceonbord=canplaceonbord.values.tolist()

    for horizontal in range(0,9):
        for virtical in range(0,9):
            try:
                if len(canplaceonbord[horizontal][virtical])==1:
                    sudokobord[virtical][horizontal]=canplaceonbord[horizontal][virtical][0]#xy
            except:
                pass
    #print(canplaceonbord)
    canplaceonbord= pd.DataFrame(index=[0,1,2,3,4,5,6,7,8], columns=[0,1,2,3,4,5,6,7,8])
print(sudokobord)
