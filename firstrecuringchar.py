#find first most addjesent recuring character from a string
string="abc"
p=1
while p<=len(string):
    for i in range(len(string)-1):
        try:
            if string[i]==string[i+p]:
                print(string[i])
                exit()
        except:
            pass
    p+=1