def init_state(input_file):
    with open(f'{input_file}') as file:
        text = file.read()
    lines = text.split('\n')
    init_space_string = [list(line) for line in lines]
    n = len(init_space_string)
    m = len(init_space_string[0])
    state = [[0]*m]*n
    for i, e in enumerate(init_space_string):
        state[i] = [1 if x == '*' else 0 for x in e]
    return state


def change_state(state):
    n = len(state)
    m = len(state[0])
    # print(n)
    # print(m)
    for i in range(n-2, -1, -1):
        for j in range(m):
            if state[i][j] == 1:

                if j == 0:
                    if state[i+1][j] == 0:
                        state[i+1][j] = 1
                        state[i][j] = 0
                    elif state[i+1][j] == 1 and state[i+1][j+1] == 0:
                        state[i+1][j+1] = 1
                        state[i][j] = 0
                    else:
                        continue
                
                elif j == (m-1):
                    if state[i+1][j] == 0:
                        state[i+1][j] = 1
                        state[i][j] = 0
                    elif state[i+1][j] == 1 and state[i+1][j-1] == 0:
                        state[i+1][j-1] = 1
                        state[i][j] = 0
                    else:
                        continue
                
                else:
                    if state[i+1][j] == 0:
                        state[i+1][j] = 1
                        state[i][j] = 0
                    elif state[i+1][j] == 1 and state[i+1][j-1] == 0 and state[i+1][j+1] == 0:
                        if (i+j) % 2 == 0:
                            state[i+1][j-1] = 1
                            state[i][j] = 0
                        else:
                            state[i+1][j+1] = 1
                            state[i][j] = 0
                    elif state[i+1][j] == 1 and state[i+1][j-1] == 0 and state[i+1][j+1] == 1:
                        state[i+1][j-1] = 1
                        state[i][j] = 0
                    elif state[i+1][j] == 1 and state[i+1][j-1] == 1 and state[i+1][j+1] == 0:
                        state[i+1][j+1] = 1
                        state[i][j] = 0
                    else:
                        continue
    return state


def output_state(state):
    n = len(state)
    m = len(state[0])
    output = [' '*m]*n
    for i, e in enumerate(state):
        output[i] = ['*' if x == 1 else ' ' for x in e]
        output[i] = ''.join(output[i])
        print(output[i], end="")
        print()
    print()