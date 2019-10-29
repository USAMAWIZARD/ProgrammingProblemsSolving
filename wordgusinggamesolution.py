#encounterd a game in which you are given some letters and
#some empty sapace of length n
#you have to guess a word that fit that n length empty space


#eg r a y i f a
# _ _ _        -ray,raf,far
# _ _ _ _ _    -fairy
# _ _ _ _      -fray

from nltk.corpus import words
import itertools
allwordsineng=words.words()
lettersavailable=input().split()
lenthofgusingwords=input().split()
print(lenthofgusingwords)
print(type(lenthofgusingwords[0]))
premutationlist=[]
noofper=set(lenthofgusingwords)
allposiblearangements=[]
index=0
for i in noofper:
    for element in list(itertools.permutations(lettersavailable,int(i))):
        allposiblearangements.append("".join(element))
print(allposiblearangements)
print(set(allposiblearangements).intersection(set(allwordsineng)))