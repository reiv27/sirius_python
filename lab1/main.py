import sys
from lab1 import get_pi
from decimal import getcontext

getcontext().prec = int(sys.argv[1])

arg = int(sys.argv[1])
print(get_pi(arg))