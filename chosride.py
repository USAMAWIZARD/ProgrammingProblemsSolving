import numpy as np
toachive=np.array([2,5,1,3,4])
og=np.arange(1,len(toachive)+1)
sub=toachive-og
addition=sum(x for x in sub if x > 0)
print("to") if sum(sub>=3) else print(addition)