# Matrix Algebra
2.1 import numpy as np
my_listu = [6,2,-3,5]
my_listv = [3,5,-1,4]
my_listu = np.array(my_listu)
my_listv = np.array(my_listv)
my_listu + my_listv
#array([ 9,  7, -4,  9])

2.2
my_listu = [6,2,-3,5]
my_listv = [3,5,-1,4]
my_listu = np.array(my_listu)
my_listv = np.array(my_listv)
my_listu - my_listv
#array([ 3, -3, -2,  1])

2.3
my_listu = [6,2,-3,5]
my_listu = np.array(my_listu)
my_listu*6
#array([ 36,  12, -18,  30])
2.4
my_listu = [6,2,-3,5]
my_listv = [3,5,-1,4]
my_listu = np.array(my_listu)
my_listv = np.array(my_listv)
np.dot(my_listu,my_listv)
#51
2.5
my_listu = [6,2,-3,5]
my_listu = np.array(my_listu)
np.linalg.norm(my_listu)
#8.6023252670426267

