import sys
import numpy as np
from math import sin, cos


class Transform2D:
    def __init__(self, rot : float, t : list):
        self.rot = rot
        self.tran = t
    
    def __mul__(self, pt):
        new_tx = cos(self.rot) * pt[0] - sin(self.rot) * pt[1] + self.tran[0]
        new_ty = sin(self.rot) * pt[0] + cos(self.rot) * pt[1] + self.tran[1]
        return [np.float64(round(new_tx, 4)), np.float64(round(new_ty, 4))]
    
    def __matmul__(self, other):
        new_rot = self.rot + other.rot
        new_tx = cos(self.rot) * other.tran[0] - sin(self.rot) * other.tran[1] + self.tran[0]
        new_ty = sin(self.rot) * other.tran[0] + cos(self.rot) * other.tran[1] + self.tran[1]
        return Transform2D(new_rot, [new_tx, new_ty])
    
    @property
    def inv(self):
        new_rot = -self.rot
        new_tx = -(cos(new_rot) * self.tran[0] - sin(new_rot) * self.tran[1])
        new_ty = -(sin(new_rot) * self.tran[0] + cos(new_rot) * self.tran[1])
        return Transform2D(new_rot, [new_tx, new_ty])
    
    def __str__(self) -> str:
        return f'rot = {round(self.rot, 4)}; tran = ({round(self.tran[0], 4)}, {round(self.tran[1], 4)})'
    

def tran(tx : float, ty : float):
    return Transform2D(0, [tx, ty])


def rot(rot : float):
    return Transform2D(rot, [0, 0])


def inv(tf : Transform2D):
    return tf.inv


def calc(expr : str):
    idx = 0
    for i, s in enumerate(expr):
        if s == '@':
            idx = i
    if expr[-1] == ']':
        expr = expr[:idx] + '*' + expr[idx+1:]
    return eval(expr)


expr = sys.argv[1]
print(calc(expr))
