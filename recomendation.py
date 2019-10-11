users={"usama":["sunil","dhur","faizan"],"sunil":["dhur","usama"],"faizan":["usama"],"dhur":["usama","sunil"]}
pendingrequest=[]
def sendRequest(destination,source):
    users[source].append("0"+destination)
def printdict():
    print(users)

def acceptOrDenyRequest():
    global pendingrequest
    print("enter username to get frind list of pending request")
    usertoacess=input()
    print("pending requests")
    for i in users[usertoacess]:
        if i[0]=='0':
            pendingrequest.append(i[1:])
    for i in pendingrequest:
        print("you have friend request from "+i)
        print("press a to accept d to deny ")
        aord=input()
        if aord=='a':
            users[usertoacess][users[usertoacess].index('0'+i)]=i
            users[i].append(usertoacess)
        if aord=='d':
            users[usertoacess].remove("0"+i)

    pendingrequest=[]

while True:
    print("1.Send a friend request")
    print("2.Print dict")
    print("3.Accept or deny friend request")
    print("3.Exit")
    choice=input()
    if choice=='1':
        print("enter  source of request")
        source=input()
        print("enter destination of request")
        destination=input()
        if source in users[destination]:
            print("you are already a friend")
        else:
            sendRequest(source,destination)
    if choice=='2':
        printdict()
    if choice=='3':
        acceptOrDenyRequest()
    if choice=='5':
        exit()
    if choice =='4':
        allusers=list(users.keys())
        for user in allusers:
            i = allusers.index(user) + 1
            while i<len(users.keys()):
                mutualfriends=list(set(users[user]).intersection(set(users[allusers[i]])))
                for chkifdfrind in mutualfriends:
                    if  (allusers[i] not in users[user]):
                        print(allusers[i],"is a mutual friend of ",user,"by ",chkifdfrind)
                i+=1