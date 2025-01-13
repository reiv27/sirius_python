import numpy as np
import matplotlib.pyplot as plt

image = plt.imread('test.png')

input_grid = np.array(image)
if input_grid.dtype != np.uint8:
    input_grid = (input_grid * 255).astype(np.uint8)
n = input_grid.shape[0]
m = input_grid.shape[1]


test_input = np.array([
    [1, 3, 3, 4],
    [7, 2, 6, 1],
    [10, 9, 1, 2],
    [4, 2, 5, 8]
])

u = test_input.copy()
n = test_input.shape[0]
m = test_input.shape[1]


u = input_grid.copy()
n = input_grid.shape[0]
m = input_grid.shape[1]

# w = np.zeros((n, m), dtype=np.uint32)
# w[0] = test_input[0].copy()
w = np.zeros((n, m), dtype=np.uint32)
w[0] = input_grid[0].copy()

c = np.zeros((n, m), dtype=np.uint16)
c[0] = [i for i in range(m)]


for i in range(1, n):

    for j in range(m):
        if j == 0:
            w[i,j] = w[i-1,j] + u[i,j] + 1
            # print(f'w[i,j] = {w[i,j]} = {u[i-1,j]} + {u[i,j]} + 1')
            c[i,j] = j
            continue
        from_up = w[i-1,j] + u[i,j] + 1
        from_left = w[i,j-1] + u[i,j] + 1
        if from_up > from_left:
            w[i,j] = from_left.copy()
            c[i,j] = j-1
        else:
            w[i,j] = from_up.copy()
            c[i,j] = j
        
    for j in range(m-2, -1, -1):
        from_right = w[i,j+1] + u[i,j] + 1
        # print(i, j)
        # print(f'{w[i,j]} from_right = {from_right} = {u[i-1,j]} + {u[i,j]} + 1')
        if from_right < w[i,j]:
            w[i,j] = from_right.copy()
            c[i,j] = j+1

            
print(u)
print(w)
print(c)


min_end = min(w[n-1,:])
# print(min_end)
for i in range(m):
    if w[n-1, i] == min_end:
        min_idx = i

y = [i for i in range(n)]
print(y)
x = [0]*n
x[n-1] = min_idx
j = min_idx
for i in range(n-2, -1, -1):
    j = c[i,j]
    x[i] = int(j)

print(x)

plt.imshow(image, cmap='grey')
plt.axis('off')
plt.plot(x, y, color='red', marker='o')
plt.show()