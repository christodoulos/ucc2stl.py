"Example usage"

from utils import dense_cuboids
from cuboids import CuboidComplex

CUBOIDS = dense_cuboids('examples/Node.txt', 'examples/Connectivity.txt',
                        'examples/density.txt', 0.3)
CUBOID_COMPLEX = CuboidComplex(CUBOIDS)
CUBOID_COMPLEX.export_off()