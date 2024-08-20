from typing import Iterable
from build123d import Shape, ShapeList, Axis

def extremum(elements: ShapeList, key: str):
    if key[0] == '-':
        elements = elements.group_by(Axis.X)[0]
    elif key[0] == '+':
        elements = elements.group_by(Axis.X)[-1]
    if key[1] == '-':
        elements = elements.group_by(Axis.Y)[0]
    elif key[1] == '+':
        elements = elements.group_by(Axis.Y)[-1]
    if key[2] == '-':
        elements = elements.group_by(Axis.Z)[0]
    elif key[2] == '+':
        elements = elements.group_by(Axis.Z)[-1]
    return elements