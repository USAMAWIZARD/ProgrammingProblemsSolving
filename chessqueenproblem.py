#maing all posible place in a chessbord
index=0
one=None
two=None
three=None
four=None
five=None
six= None
seven=None
eight=None
allposiblequeenplacement=[None]
def chkequality(list):
    i=-1
    for element in list:
        if element==None:
            continue
        i += 1
        if  list.count(i)>1:
          return False
    return True

xx=[0,1,2,3,4,5,6,7]
index=0

for one in xx:
    if chkequality([one,two,three,four,five,six,seven,eight]):
        for two in xx:
            if chkequality([one,two,three,four,five,six,seven,eight]):
                for three in xx:
                    if chkequality([one,two,three,four,five,six,seven,eight]):
                        for four in xx:
                            if chkequality([one,two,three,four,five,six,seven,eight]):
                                for five in xx:
                                    if chkequality([one,two,three,four,five,six,seven,eight]):
                                        for six in xx:
                                            if chkequality([one,two,three,four,five,six,seven,eight]):
                                                for seven in xx:
                                                    if chkequality([one,two,three,four,five,six,seven,eight]):
                                                        for eight in xx:
                                                            if chkequality([one,two,three,four,five,six,seven,eight]):
                                                                allposiblequeenplacement=allposiblequeenplacement+[None]
                                                                allposiblequeenplacement[index]=[one,two,three,four,five,six,seven,eight]
                                                                print(allposiblequeenplacement[index])
                                                                index+=1
                                                        if chkequality([one, two, three, four, five, six, seven,eight]):
                                                            allposiblequeenplacement = allposiblequeenplacement + [None]
                                                            allposiblequeenplacement[index] = [one, two, three, four,
                                                                                               five, six, seven, eight]
                                                            print(allposiblequeenplacement[index])
                                                            index += 1
                                                if chkequality([one, two, three, four, five, six, seven,eight]):
                                                    allposiblequeenplacement = allposiblequeenplacement + [None]
                                                    allposiblequeenplacement[index] = [one, two, three, four, five, six,
                                                                                       seven, eight]
                                                    print(allposiblequeenplacement[index])
                                                    index += 1
                                        if chkequality([one, two, three, four, five, six, seven,eight]):
                                            allposiblequeenplacement = allposiblequeenplacement + [None]
                                            allposiblequeenplacement[index] = [one, two, three, four, five, six, seven,
                                                                               eight]
                                            print(allposiblequeenplacement[index])
                                            index += 1
                                if chkequality([one, two, three, four, five, six, seven,eight]):
                                    allposiblequeenplacement = allposiblequeenplacement + [None]
                                    allposiblequeenplacement[index] = [one, two, three, four, five, six, seven, eight]
                                    print(allposiblequeenplacement[index])
                                    index += 1
                        if chkequality([one, two, three, four, five, six, seven,eight]):
                            allposiblequeenplacement = allposiblequeenplacement + [None]
                            allposiblequeenplacement[index] = [one, two, three, four, five, six, seven, eight]
                            print(allposiblequeenplacement[index])
                            index += 1
                if chkequality([one, two, three, four, five, six, seven,eight]):
                    allposiblequeenplacement = allposiblequeenplacement + [None]
                    allposiblequeenplacement[index] = [one, two, three, four, five, six, seven, eight]
                    print(allposiblequeenplacement[index])
                    index += 1
            if chkequality([one, two, three, four, five, six, seven,eight]):
                allposiblequeenplacement = allposiblequeenplacement + [None]
                allposiblequeenplacement[index] = [one, two, three, four, five, six, seven, eight]
                print(allposiblequeenplacement[index])
                index += 1
        if chkequality([one, two, three, four, five, six, seven,eight]):
            allposiblequeenplacement = allposiblequeenplacement + [None]
            allposiblequeenplacement[index] = [one, two, three, four, five, six, seven, eight]
            print(allposiblequeenplacement[index])
            index += 1
    if chkequality([one, two, three, four, five, six, seven,eight]):
        allposiblequeenplacement = allposiblequeenplacement + [None]
        allposiblequeenplacement[index] = [one, two, three, four, five, six, seven, eight]
        print(allposiblequeenplacement[index])
        index += 1