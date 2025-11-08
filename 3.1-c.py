import numpy as np

a = np.array([1.0, 2.0, 3.0, 4.0])
b = np.array([2.0, 2.0, 1.0, 4.0])

greater_result = np.greater(a, b)
greater_equal_result = np.greater_equal(a, b)
less_result = np.less(a, b)
less_equal_result = np.less_equal(a, b)
equal_result = np.equal(a, b)
allclose_result = np.allclose(a, b, atol=1e-8)

print(greater_result)
print(greater_equal_result)
print(less_result)
print(less_equal_result)
print(equal_result)
print(allclose_result)
