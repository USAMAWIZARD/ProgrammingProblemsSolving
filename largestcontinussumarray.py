array=[-2,-3,5,-2,-2,1,5,-3]   # 7
largest=array[0]
i=j=0
summ=0
continusno=[]
while i<len(array):
    j=i
    continusno=[]
    while j<len(array):
        summ=summ+array[j]
        continusno.append(array[j])
        j+=1
        if summ>largest :
            arr=continusno
            largest = summ
    summ=0
    i+=1
print(arr)
print(largest)