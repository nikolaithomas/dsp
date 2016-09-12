# Matrix Algebra
2.1 
import numpy as np
my_listu = [6,2,-3,5]
my_listv = [3,5,-1,4]
my_listu = np.array(my_listu)
my_listv = np.array(my_listv)
my_listu + my_listv
#array([ 9,  7, -4,  9])

2.2
import numpy as np
my_listu = [6,2,-3,5]
my_listv = [3,5,-1,4]
my_listu = np.array(my_listu)
my_listv = np.array(my_listv)
my_listu - my_listv
#array([ 3, -3, -2,  1])

2.3
import numpy as np
my_listu = [6,2,-3,5]
my_listu = np.array(my_listu)
my_listu*6
#array([ 36,  12, -18,  30])

2.4
import numpy as np
my_listu = [6,2,-3,5]
my_listv = [3,5,-1,4]
my_listu = np.array(my_listu)
my_listv = np.array(my_listv)
np.dot(my_listu,my_listv)
#51

2.5
import numpy as np
my_listu = [6,2,-3,5]
my_listu = np.array(my_listu)
np.linalg.norm(my_listu)
#8.6023252670426267

3.1
import numpy as np
arrA = np.array([[1,2,3],[2,7,4]])
arrC = np.array([[5,-1],[9,1],[6,0]])
arrA + arrC
#ValueError: operands could not be broadcast together with shapes (2,3) (3,2) 

3.2
import numpy as np
arrA = np.array([[1,2,3],[2,7,4]])
arrC = np.array([[5,-1],[9,1],[6,0]])
arrA - np.transpose(arrC)
#array([[-4, -7, -3],
       [ 3,  6,  4]])
       
3.3
import numpy as np
arrD = np.array([[3,-2,-1],[1,2,3]])
arrC = np.array([[5,-1],[9,1],[6,0]])
3*arrD + np.transpose(arrC)
#array([[14,  3,  3],
       [ 2,  7,  9]])

3.4
import numpy as np
arrA = np.array([[1,2,3],[2,7,4]])
arrB = np.array([[1,-1],[0,1]])
arrA*arrB
#ValueError: operands could not be broadcast together with shapes (2,3) (2,2) 

3.5
import numpy as np
arrA = np.array([[1,2,3],[2,7,4]])
arrB = np.array([[1,-1],[0,1]])
np.transpose(arrA) * arrB
#ValueError: operands could not be broadcast together with shapes (3,2) (2,2)



