'''
i saw a mathametical fact on instagram which says 73939133 is the largest
known prime number  that if you keep removing digits from the right will
always leave a prime no.
i came up with an idea of proving this fact using a program
'''

global isnothat
global i
isnothat=0
def removelastelement(strnum):
    return strnum[:len(strnum)-1]           #removing the last char from str num

def prime(number):
    primeno=1
    itrate=number//2                         #find prime of not
    while itrate>1:
        if number % itrate == 0:
            primeno=0
            break
        itrate-=1
    if primeno:
        divideanditrate(number)         #ye line pe thoda sa problem hai
    else:
        return 0


def divideanditrate(number):
    global isnothat
    isnothat+=1
    strnum=str(number)
    strnumrem = removelastelement(strnum)

    for evrnum in range(len(strnumrem)):
        if not prime(int(strnumrem)):
            isnothat=0
            return
        else:
            return
    if isnothat==len(str(i)):
        print(i)
    isnothat=0
for i in range(1,1000000000000000000000000):
    prime(i)
