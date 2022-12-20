import numpy as np
import pandas as pd
# import time
import matplotlib.pyplot as plt
# from numba import jit

# @jit(nopython=True)
test1 = pd.read_csv("test1.csv")
X=np.matrix(test1.iloc[:,0:1]).reshape(1,70)
y=np.matrix(test1.iloc[:,-1])
theta=np.matrix([0,0])
print(X.shape)
print(y.shape)
print(theta.shape)





def GD(x,y):
    iter=10
    m=len(x)
    
    for i in range (iter):
        for i in range (len(x)):
            f_x=(np.dot(theta,x[i]))
            print(f_x)



# evaluationStart = time.time()
# GD(X ,y)
# # evaluationEnd = time.time()

# print(f"Time: {evaluationEnd - evaluationStart}")
