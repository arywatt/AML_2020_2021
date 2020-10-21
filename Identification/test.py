## import packages
import numpy as np



D = np.array([[1,3,2,1],[2,4,6,8],[1,3,2,1],[1,3,2,1]])
print(D.size)

labels = np.diag([1]*4)
      
d = D.reshape(D.size)
l = labels.reshape(labels.size)
print('D :',D)
print('l :',l)
     
sortidx = d.argsort()
d = d[sortidx]
l = l[sortidx]

print(sortidx)
print(d)
print(l)