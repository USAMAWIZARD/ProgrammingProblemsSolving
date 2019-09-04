weight = [[13, 4], [1, 2, 3, 6, 14]]

addition = 0
i = 4

if weight[0][0]>weight[0][1]:
    temp=weight[0][1]
    weight[0][1]=weight[0][0]
    weight[0][0]=temp
addition = weight[0][0]

while addition != weight[0][1]:
    if (weight[0][0] + weight[1][i]) <= weight[0][1]:
        print(weight[1][i])
        addition = int(weight[1][i]) + addition
    i -= 1
if addition==weight[0][1]:
    exit()



