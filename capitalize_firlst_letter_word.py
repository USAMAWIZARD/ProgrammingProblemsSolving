string="usama is a computer wizard"
string=string[0].upper()
def capitalize(sent,loc):
    return sent[:loc]+sent[loc].upper()+sent[loc+1:]
i=0
while i < len(string):
    if string[i]==' ':
        string=capitalize(string,i+1)
    i+=1

print(string)