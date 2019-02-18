import numpy as np

def step(x):
    y = x > 0 #generate Boolean 
    return y.astype(np.int) #bool to int(True -> 1,False -> 0)


