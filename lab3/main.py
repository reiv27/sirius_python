import sys
from calc import read_data, constuct_a

input_file = sys.argv[1]
p = int(sys.argv[2])

input_data = read_data(input_file)

g = [0.0]*len(input_data)
c = [0.0]*p
for j in range(p):
     get_c = constuct_a(input_data, j)
     c[j] = str(round(get_c(), 4))
     print(c[j], end=' ')
