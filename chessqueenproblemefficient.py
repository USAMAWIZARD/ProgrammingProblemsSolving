import pandas as pd
import numpy as np
#initialization
allposiblequeenplacement = [None]
xx = [0, 1, 2, 3, 4, 5, 6, 7]
index=0

def checkColutionQueen(list):
    i = -1
    for element in list:
        i += 1
        if list.count(i) > 1:       #vertical colution removal
            return False

    result=np.array(list)-[0,1,2,3,4,5,6,7]
    result=result.tolist()

    for element in result:
        if result.count(element) > 1:           #digonal coloution removeal (hear right)
            return False

    result = np.array(list) + [0, 1, 2, 3, 4, 5, 6, 7]
    result = result.tolist()
    for element in result:                      #digonal coloution removal  (head left)
        if result.count(element) > 1:
            return False
    return True

for one in xx:
    for two in xx:
        for three in xx:
            for four in xx:# maing all posible place in a chessbord
                for five in xx:
                    for six in xx:
                        for seven in xx:
                            for eight in xx:
                                if checkColutionQueen([one, two, three, four, five, six, seven, eight]):
                                    allposiblequeenplacement = allposiblequeenplacement + [None]
                                    allposiblequeenplacement[index] = [one, two, three, four, five, six, seven, eight]
                                    index += 1
print(allposiblequeenplacement)