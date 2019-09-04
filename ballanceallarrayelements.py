import numpy as np
choice = [1, 2, 5]

numlist = np.array([1, 1, 5])
listaftersub = numlist - min(numlist)

def getlist(no):
    listtoreturn = []
    i = len(choice)-1
    p=0
    sumelements=0
    elemetns=no
    while sumelements!=elemetns:
        if (choice[i] + sumelements <= elemetns):
            sumelements = choice[i] + sumelements
            listtoreturn=listtoreturn+[None]
            listtoreturn[p]=choice[i]
            p+=1
        else:
            i -= 1
    return listtoreturn
i=0
print(sum(getlist(10)))
exit()
while i < len(numlist):
    for p in numlist:
        addnumber = listaftersub[i]
        numlist = sum(getlist(p)) + addnumber
        numlist[i] = numlist[i] - addnumber
        print(numlist)
        i += 1
print(listaftersub)
