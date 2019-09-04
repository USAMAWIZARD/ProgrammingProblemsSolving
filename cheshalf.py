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
def chkequalityandadjecency(list):
    i=-1
    for element in list:
        i += 1
        if  list.count(i)>1:
          return False
    if list[1]==list[0]+1 or list[0]==list[1]+1 or list[2]==list[1]+1 or list[1]==list[2]+1 or list[3]==list[2]+1 or list[2]==list[3]+1 or list[3]==list[4]+1 or list[4]==list[3]+1 or list[4]==list[5]+1 or list[5]==list[4]+1 or list[5]==list[6]+1 or list[6]==list[5]+1 or  list[6]==list[7]+1 or list[7]==list[6]+1:
        return False
    return True

xx=[0,1,2,3,4,5,6,7]
index=0

for one in xx:
    for two in xx:
        for three in xx:
            for four in xx:
                for five in xx:
                    for six in xx:
                        for seven in xx:
                            for eight in xx:
                                if chkequalityandadjecency([one, two, three, four, five, six, seven, eight]):
                                    allposiblequeenplacement=allposiblequeenplacement+[None]
                                    allposiblequeenplacement[index]=[one,two,three,four,five,six,seven,eight]
                                    print(allposiblequeenplacement[index])
                                    index+=1

