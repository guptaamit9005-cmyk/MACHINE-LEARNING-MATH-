import numpy as np 
A = np.array([1,2,3])
B = np.array([4,5,6])

distance = np.linalg.norm(A-B)
print(distance)

# USING WITHOUT NUMPY 
import numpy 
A = [1,2,3]
B = [4,5,6]
distance = math.sqrt(sum((A-B)**2))
print(distance)