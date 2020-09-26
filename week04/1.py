import numpy as np
i=0
a=[1,100,1000]
y=[]
for x in a:
    y.append(float(np.log(np.exp(1/(np.sin(x)+1))/(5/4+x**15))/(1+x**2)))
print(y)