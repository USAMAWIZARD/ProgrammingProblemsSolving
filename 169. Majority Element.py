'''Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3
'''

nums=[3,2,3]
numcounts={}
for i in nums:
    if i in numcounts:
        numcounts[i]+=1
    else:
        numcounts[i]=0
    
print(max(numcounts, key=numcounts.get))
