import numpy as np

x=np.array([1,2,3,4])

x
Out[3]: array([1, 2, 3, 4])

x=np.array([3.5,1,2,3,4])

x
Out[5]: array([3.5, 1. , 2. , 3. , 4. ])

x=np.array([1,2,3,4],dtype=float)

x
Out[7]: array([1., 2., 3., 4.])

x=np.ones((3,3),dtype=int)

x
Out[9]: 
array([[1, 1, 1],
       [1, 1, 1],
       [1, 1, 1]])

x=np.zeros((3,3),dtype=int)

x
Out[11]: 
array([[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0]])

x=np.full((3,3),3)

x
Out[13]: 
array([[3, 3, 3],
       [3, 3, 3],
       [3, 3, 3]])