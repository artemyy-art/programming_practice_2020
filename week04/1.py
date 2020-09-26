import numpy as np
i=0
x=1
y=[]
while i<3:
    x=x*10
    y.append(float(np.log(np.exp(1/(np.sin(x)+1))/(5/4+x**15))/(1+x**2)))
    i=i+1
print(y)