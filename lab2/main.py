import sys
from copy import copy
from time import sleep
from lab2 import init_state, output_state, change_state


file = sys.argv[1]
state = init_state(file)
while True:
    old_state = copy.deepcopy(state)
    output_state(old_state)
    state = change_state(state)
    sleep(1)
    if old_state == state:
        break