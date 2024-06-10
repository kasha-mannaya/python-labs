import numpy as np

data = np.array(list(map(int, input("Please, enter the x vector:").split())))
indexes = np.append(np.where(data[1:] != data[:-1]), len(data) - 1)
difference = np.diff(np.append(-1, indexes))       

print(data[indexes])
print(difference)