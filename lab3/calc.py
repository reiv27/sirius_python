import csv
from scipy.special import legendre


def read_data(file):
    data = []
    with open(file, mode='r') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            data.append((float(line[0]), float(line[1])))
    return sorted(data, key=lambda x: x[0])


def constuct_a(data, p):
    n = len(data)
    a = 0.0
    pol_leg = legendre(p)
    for i in range(n-1):
        h = data[i+1][0] - data[i][0]
        a += h * (data[i+1][1]*pol_leg(data[i+1][0]) + data[i][1]*pol_leg(data[i][0]))
    a /= 2.0
    
    def get_c():
        return (2.0*p + 1.0)/2.0 * a
    
    return get_c