import numpy as np
import pandas as pd
import Data_cleaning as df

x=df.x
y=df.y.reshape(-1, 1)
x_bais=np.hstack([(np.ones((x.shape[0],1))),x])
i=np.eye(x_bais.shape[1])
i[0,0]=0
lams=[0,0.1,0.001]
# lam=0.1
# w=np.linalg.inv(x_bais.T@x_bais+lam*i)@x_bais.T@y

# y_predict=x_bais@w
# mse=np.mean((y-y_predict)**2)
# print(mse)

def mse_check(y,y_preict):
    return np.mean((y-y_preict)**2)

def ridge_regression(x_bais,y,lam):
    w=np.linalg.inv(x_bais.T@x_bais+lam*i)@x_bais.T@y
    return w
best_lam=None,
def lam_passing(x_bais,y,lams):
    best_error=float('inf')
    best_lam=best_w=None
    for i in lams:
        w=ridge_regression(x_bais,y,i)
        y_predict=x_bais@w
        mse=mse_check(y,y_predict)
        if mse<best_error:
            best_error=mse
            best_lam=i
            best_w=w
    return best_error, best_lam,best_w

mse,lam,w=lam_passing(x_bais,y,lams)        

