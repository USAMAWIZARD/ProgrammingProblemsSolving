'''Good morning! Heres your coding interview problem for today.
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
5or example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].'''

numberlist=[1, 2, 3, 4, 5]
productarray=[1]*len(numberlist)
for i in range(len(numberlist)):
    for j in range(len(numberlist)):
        if(i==j):
            continue
        productarray[i]*=numberlist[j]
print(productarray)