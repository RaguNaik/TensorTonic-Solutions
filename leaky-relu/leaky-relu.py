import numpy as np

def leaky_relu(x, alpha=0.01):
    # Ensure x is a numpy array so 'x >= 0' works element-wise
    x = np.asarray(x) 
    return np.where(x >= 0, x, alpha * x)

# This will now work even if you pass a plain list
data_list = [-2, -1, 0, 1, 2]
result = leaky_relu(data_list)

print(result)
# Output: [-0.02, -0.01,  0.  ,  1.  ,  2.  ]