import matplotlib.pyplot as plt
import numpy as np
#  samkutxedi <3
xpoints = [0, 10, 80, 0]
ypoints = [0, 64, 20, 0]
s= 0
i = 0
f= 64
o=0
l=20
for i in range(15):
    
    s+=5
    f+=5
    l+=1
    o+=5
    ypoints.append(s)
    ypoints.append(f)
    ypoints.append(l)
    ypoints.append(o)
    xpoints.append(0)
    xpoints.append(10)
    xpoints.append(80)
    xpoints.append(0)
    

plt.plot(xpoints, ypoints)
plt.show()