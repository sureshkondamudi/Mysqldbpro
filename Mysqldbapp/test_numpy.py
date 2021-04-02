import numpy as np
import matplotlib.pyplot as plt
a=np.array([(1,2,4),(5,6,7),(7,8,9)])
print(a.shape)


# adding two arrys
a1=np.array([(1,2,3),(4,5,6)])
b1=np.array([(9,8,7),(1,2,3)])
print(a1+b1)
# add two elements in on array
arr =np.array([1,2,3,5,6,7])
print(arr[2]+arr[3])

# special functions
ar=np.arange(0,3*np.pi,0.1)
ar1=np.tan(ar)
plt.plot(ar,ar1)
plt.show()

# slicing

sl=np.array([(1,2,3),(5,6,7)])
print(sl[0:,1])



