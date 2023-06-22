import ctypes
import random

# Load the dynamic library
operations = ctypes.CDLL('./100-operations.so')

# Define the function signature
random_operation = operations.random_operation
random_operation.argtypes = (ctypes.POINTER(ctypes.c_int),)
random_operation.restype = ctypes.c_int

# Generate two random integers and perform the operation
result = ctypes.c_int()
random_operation(ctypes.byref(result))
print(f"The result of the random operation is: {result.value}")
