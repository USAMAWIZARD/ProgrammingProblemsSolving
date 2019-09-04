import pandas as pd
import numpy as np
#initialization
feature_list = [0, 1, 2, 3, 4, 5, 6, 7]
allposiblequeenplacement = [None]
xx = [0, 1, 2, 3, 4, 5, 6, 7]
chessbord = pd.DataFrame(0, index=np.arange(len([1, 2, 3, 4, 5, 6, 7, 8])), columns=feature_list)
q1 = "70"
q2 = "61"
q3 = "52"
q4 = "43"
q5 = "34"
q6 = "25"
q7 = "16"
q8 = "07"

listindex = 0
index=0

#functions
def overwrite():
    global chessbord
    chessbord = pd.DataFrame(0, index=np.arange(len([1, 2, 3, 4, 5, 6, 7, 8])), columns=feature_list)
def chkequalityandadjecency(list):
    i = -1
    for element in list:
        i += 1
        if list.count(i) > 1:
            return False
    if list[1] == list[0] + 1 or list[0] == list[1] + 1 or list[2] == list[1] + 1 or list[1] == list[2] + 1 or list[
        3] == list[2] + 1 or list[2] == list[3] + 1 or list[3] == list[4] + 1 or list[4] == list[3] + 1 or list[4] == \
            list[5] + 1 or list[5] == list[4] + 1 or list[5] == list[6] + 1 or list[6] == list[5] + 1 or list[6] == \
            list[7] + 1 or list[7] == list[6] + 1:
        return False
    return True
def checkQueenColution():
    horizontal = chkhorizontal()
    vetical = chkvirtical()
    rightdigonal = chkrightdigonal()
    leftdigonal = chkleftdigonal()
    #print(horizontal,vetical,rightdigonal,leftdigonal)
    if horizontal and vetical and rightdigonal and leftdigonal:
        print(chessbord)
        print("problem solved success fully")
def chkhorizontal():
    x = 0
    sum = 0
    while x <= 7:
        sum = sum + chessbord[x][int(q1[1])]
        x += 1
    if sum != 1:
        return False
    x = 0
    sum = 0
    while x <= 7:
        sum = sum + chessbord[x][int(q2[1])]
        x += 1
    if sum != 1:
        return False
    x = 0
    sum = 0
    while x <= 7:
        sum = sum + chessbord[x][int(q3[1])]
        x += 1
    if sum != 1:
        return False
    x = 0
    sum = 0
    while x <= 7:
        sum = sum + chessbord[x][int(q4[1])]
        x += 1
    if sum != 1:
        return False
    x = 0
    sum = 0
    while x <= 7:
        sum = sum + chessbord[x][int(q5[1])]
        x += 1
    if sum != 1:
        return False
    x = 0
    sum = 0
    while x <= 7:
        sum = sum + chessbord[x][int(q6[1])]
        x += 1
    if sum != 1:
        return False
    x = 0
    sum = 0
    while x <= 7:
        sum = sum + chessbord[x][int(q7[1])]
        x += 1
    if sum != 1:
        return False
    x = 0
    sum = 0
    while x <= 7:
        sum = sum + chessbord[x][int(q8[1])]
        x += 1
    if sum != 1:
        return False
    return True
def chkvirtical():
    y = 0
    sum = 0
    while y <= 7:
        sum = sum + chessbord[int(q1[1])][y]
        y += 1
    if sum != 1:
        return False
    y = 0
    sum = 0
    while y <= 7:
        sum = sum + chessbord[int(q2[1])][y]
        y += 1
    if sum != 1:
        return False
    y = 0
    sum = 0
    while y <= 7:
        sum = sum + chessbord[int(q3[1])][y]
        y += 1
    if sum != 1:
        return False
    y = 0
    sum = 0
    while y <= 7:
        sum = sum + chessbord[int(q4[1])][y]
        y += 1
    if sum != 1:
        return False
    y = 0
    sum = 0
    while y <= 7:
        sum = sum + chessbord[int(q5[1])][y]
        y += 1
    if sum != 1:
        return False
    y = 0
    sum = 0
    while y <= 7:
        sum = sum + chessbord[int(q6[1])][y]
        y += 1
    if sum != 1:
        return False
    y = 0
    sum = 0
    while y <= 7:
        sum = sum + chessbord[int(q7[1])][y]
        y += 1
    if sum != 1:
        return False
    y = 0
    sum = 0
    while y <= 7:
        sum = sum + chessbord[int(q8[1])][y]
        y += 1
    if sum != 1:
        return False
    y = 0
    sum = 0
    return True
def chkrightdigonal():  #head right
    if int(q1[1])<int(q1[0]): #x>y
        x=int(q1[0])-int(q1[1])
        y=0
    elif int(q1[1])>int(q1[0]):#y>x
        x=0
        y=int(q1[1])-int(q1[0])
    else:
        x=0
        y=0

    sum = 0
    while y <= 7 and x <= 7:
        sum = sum + chessbord[x][y]
        y += 1
        x += 1
    if sum != 1:
        return False

    if int(q2[1]) < int(q2[0]):  # x>y
        x = int(q2[0]) - int(q2[1])
        y = 0
    elif int(q2[1]) > int(q2[0]):  # y>x
        x = 0
        y = int(q2[1]) - int(q2[0])
    else:
        x = 0
        y = 0
    sum = 0
    while y <= 7 and x <= 7:
        sum = sum + chessbord[x][y]
        y += 1
        x += 1
    if sum != 1:
        return False

    if int(q3[1]) < int(q3[0]):  # x>y
        x = int(q3[0]) - int(q3[1])
        y = 0
    elif int(q3[1]) > int(q3[0]):  # y>x
        x = 0
        y = int(q3[1]) - int(q3[0])
    else:
        x = 0
        y = 0
    sum = 0
    while y <= 7 and x <= 7:
        sum = sum + chessbord[x][y]
        y += 1
        x += 1
    if sum != 1:
        return False

    if int(q4[1]) < int(q4[0]):  # x>y
        x = int(q4[0]) - int(q4[1])
        y = 0
    elif int(q4[1]) > int(q4[0]):  # y>x
        x = 0
        y = int(q4[1]) - int(q4[0])
    else:
        x = 0
        y = 0
    sum = 0
    while y <= 7 and x <= 7:
        sum = sum + chessbord[x][y]
        y += 1
        x += 1
    if sum != 1:
        return False

    if int(q5[1]) < int(q5[0]):  # x>y
        x = int(q5[0]) - int(q5[1])
        y = 0
    elif int(q5[1]) > int(q5[0]):  # y>x
        x = 0
        y = int(q5[1]) - int(q5[0])
    else:
        x = 0
        y = 0
    sum = 0
    while y <= 7 and x <= 7:
        sum = sum + chessbord[x][y]
        y += 1
        x += 1
    if sum != 1:
        return False

    if int(q6[1]) < int(q6[0]):  # x>y
        x = int(q6[0]) - int(q6[1])
        y = 0
    elif int(q6[1]) > int(q6[0]):  # y>x
        x = 0
        y = int(q6[1]) - int(q6[0])
    else:
        x = 0
        y = 0
    sum = 0
    while y <= 7 and x <= 7:
        sum = sum + chessbord[x][y]
        y += 1
        x += 1
    if sum != 1:
        return False

    if int(q7[1]) < int(q7[0]):  # x>y
        x = int(q7[0]) - int(q7[1])
        y = 0
    elif int(q7[1]) > int(q7[0]):  # y>x
        x = 0
        y = int(q7[1]) - int(q7[0])
    else:
        x = 0
        y = 0
    sum = 0
    while y <= 7 and x <= 7:
        sum = sum + chessbord[x][y]
        y += 1
        x += 1
    if sum != 1:
        return False
    return True
def chkleftdigonal():       #head left
    if int(q1[1]) + int(q1[0])<=7:  # x>y
        x = int(q1[0]) + int(q1[1])
        y = 0
    else :
        x = 7
        y = (int(q1[1]) + int(q1[0]))-7
    sum = 0

    while y <= 7 and x >= 0:
        sum = sum + chessbord[x][y]
        y += 1
        x -= 1
    if sum != 1:
        return False

    if int(q2[1]) + int(q2[0]) <= 7:  # x>y
        x = int(q2[0]) + int(q2[1])
        y = 0
    else:
        x = 7
        y = (int(q2[1]) + int(q2[0])) - 7
    sum = 0
    while y <= 7 and x >= 0:
        sum = sum + chessbord[x][y]
        y += 1
        x -= 1
    if sum != 1:
        return False

    if int(q3[1]) + int(q3[0]) <= 7:  # x>y
        x = int(q3[0]) + int(q3[1])
        y = 0
    else:
        x = 7
        y = (int(q3[1]) + int(q3[0])) - 7
    sum = 0
    while y <= 7 and x >= 0:
        sum = sum + chessbord[x][y]
        y += 1
        x -= 1
    if sum != 1:
        return False

    if int(q4[1]) + int(q4[0]) <= 7:  # x>y
        x = int(q4[0]) + int(q4[1])
        y = 0
    else:
        x = 7
        y = (int(q4[1]) + int(q4[0])) - 7
    sum = 0
    while y <= 7 and x >= 0:
        sum = sum + chessbord[x][y]
        y += 1
        x -= 1
    if sum != 1:
        return False

    if int(q5[1]) + int(q5[0]) <= 7:  # x>y
        x = int(q5[0]) + int(q5[1])
        y = 0
    else:
        x = 7
        y = (int(q5[1]) + int(q5[0])) - 7
    sum = 0
    while y <= 7 and x >= 0:
        sum = sum + chessbord[x][y]
        y += 1
        x -= 1
    if sum != 1:
        return False

    if int(q6[1]) + int(q6[0]) <= 7:  # x>y
        x = int(q6[0]) + int(q6[1])
        y = 0
    else:
        x = 7
        y = (int(q6[1]) + int(q6[0])) - 7
    sum = 0
    while y <= 7 and x >= 0:
        sum = sum + chessbord[x][y]
        y += 1
        x -= 1
    if sum != 1:
        return False

    if int(q7[1]) + int(q7[0]) <= 7:  # x>y
        x = int(q7[0]) + int(q7[1])
        y = 0
    else:
        x = 7
        y = (int(q7[1]) + int(q7[0])) - 7
    sum = 0
    while y <= 7 and x >= 0:
        sum = sum + chessbord[x][y]
        y += 1
        x -= 1
    if sum != 1:
        return False
    return True



#combinations
for one in xx:
    for two in xx:
        for three in xx:
            for four in xx:# maing all posible place in a chessbord
                for five in xx:
                    for six in xx:
                        for seven in xx:
                            for eight in xx:
                                if chkequalityandadjecency([one, two, three, four, five, six, seven, eight]):
                                    allposiblequeenplacement = allposiblequeenplacement + [None]
                                    allposiblequeenplacement[index] = [one, two, three, four, five, six, seven, eight]
                                    index += 1
#itration on conbination
while True:
    q1 = str(allposiblequeenplacement[listindex][0]) + "0"
    q2 = str(allposiblequeenplacement[listindex][1]) + "1"
    q3 = str(allposiblequeenplacement[listindex][2]) + "2"
    q4 = str(allposiblequeenplacement[listindex][3]) + "3"
    q5 = str(allposiblequeenplacement[listindex][4]) + "4"
    q6 = str(allposiblequeenplacement[listindex][5]) + "5"
    q7 = str(allposiblequeenplacement[listindex][6]) + "6"
    q8 = str(allposiblequeenplacement[listindex][7]) + "7"

    chessbord[allposiblequeenplacement[listindex][0]][0] = 1
    chessbord[allposiblequeenplacement[listindex][1]][1] = 1
    chessbord[allposiblequeenplacement[listindex][2]][2] = 1
    chessbord[allposiblequeenplacement[listindex][3]][3] = 1
    chessbord[allposiblequeenplacement[listindex][4]][4] = 1
    chessbord[allposiblequeenplacement[listindex][5]][5] = 1
    chessbord[allposiblequeenplacement[listindex][6]][6] = 1
    chessbord[allposiblequeenplacement[listindex][7]][7] = 1
    checkQueenColution()
    overwrite()
    listindex += 1
