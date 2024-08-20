from typing import Iterable
from build123d import Face, Wire, VectorLike

def SanePolygon(pts: Iterable[VectorLike]):
    return Face(Wire.make_polygon(pts))