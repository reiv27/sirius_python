import sys
import json
import numpy as np
from dataclasses import dataclass
from casadi import SX, cos, sin, jacobian, Function, vertcat


@dataclass
class Parameters:
    links : np.ndarray

    def __post_init__(self):
        self.lengths = np.array(self.links)
        self.n = len(self.lengths)

def read_pars_from_json(file_path):
    with open(file_path, 'r') as f:
        js = json.load(f)
        parameters = Parameters(**js)
    return parameters


class Robot:
    def __init__(self, parameters : Parameters):
        self.parameters = parameters
        self.q = SX.sym('q', self.parameters.n)
        self.d_q = SX.sym('dq', self.parameters.n)
        self.x = SX.sym('x')
        self.y = SX.sym('f_y')
        self.t = SX.sym('f_theta')
        self.df = SX.sym('dF')

    def take_state_and_velocity(self):
        xt = 0
        yt = 0
        tt = 0
        for i in range(self.parameters.n):
            tt += self.q[i]
            xt += self.parameters.lengths[i] * cos(tt)
            yt += self.parameters.lengths[i] * sin(tt)
        
        self.x = Function('x', [self.q], [xt])
        self.y = Function('y', [self.q], [yt])
        self.t = Function('t', [self.q], [tt]) 
        
        f = vertcat(xt, yt, tt)
        jac = jacobian(f, self.q) @ self.d_q
        self.df = Function('df', [self.q, self.d_q], [jac])

    def get_pose(self, q):
        print(f'pose: {self.x(q)}, {self.y(q)}, {self.t(q)}')
    
    def get_velocities(self, q, d_q):
        print(f'velocity: {self.df(q, d_q)[0]}, {self.df(q, d_q)[1]}, {self.df(q, d_q)[2]}')


q  = np.array(eval(sys.argv[1]), dtype=float)
d_q = np.array(eval(sys.argv[2]), dtype=float)
manipulator = Robot(read_pars_from_json('config.json'))
manipulator.take_state_and_velocity()
manipulator.get_pose(q)
manipulator.get_velocities(q, d_q)