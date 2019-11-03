# find first and  most repeating charachter from a string

import numpy as np
string = "aabbbbbcaacbbcccccc"
n = len(string)
dic = {}
ocr = {}
index = 0

for i in string:
    dic[i] = string.count(i)
while n != 0:
    ocr[string[0]] = index
    string = string.replace(string[0], "")
    n = len(string)
    index += 1

print('seq of occurance', ocr)
print('repetetion of unique char', dic)

final = list(np.array(list(dic.values())) - np.array(list(ocr.values()))).index(
    max(np.array(list(dic.values())) - np.array(list(ocr.values()))))
keysvalues = list(dic.keys())
print(keysvalues[final])
