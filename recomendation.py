users={"usama":["sunil","dhur","faizan"],"sunil":["dhur","usama"],"faizan":["usama"],"dhur":["usama","sunil"]}
allusers=list(users.keys())
for user in allusers:
    i = allusers.index(user) + 1
    while i<len(users.keys()):
        mutualfriends=list(set(users[user]).intersection(set(users[allusers[i]])))
        for chkifdfrind in mutualfriends:
            if  (allusers[i] not in users[user]):
                print(allusers[i],"is a mutual friend of ",user,"by ",chkifdfrind)
        i+=1