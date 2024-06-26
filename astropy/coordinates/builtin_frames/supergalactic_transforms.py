# Licensed under a 3-clause BSD style license - see LICENSE.rst

from astropy.coordinates.matrix_utilities import (rotation_matrix,
                                                  matrix_product,
                                                  matrix_transpose)
from astropy.coordinates.baseframe import frame_transform_graph
from astropy.coordinates.transformations import StaticMatrixTransform

from .galactic import Galactic
from .supergalactic import Supergalactic


@frame_transform_graph.transform(StaticMatrixTransform, Galactic, Supergalactic)
def gal_to_supergal():
    mat1 = rotation_matrix(90, 'z')
    mat2 = rotation_matrix(90 - Supergalactic._nsgp_gal.b.degree, 'y')
    mat3 = rotation_matrix(Supergalactic._nsgp_gal.l.degree, 'z')
    return matrix_product(mat1, mat2, mat3)


@frame_transform_graph.transform(StaticMatrixTransform, Supergalactic, Galactic)
def supergal_to_gal():
    return matrix_transpose(gal_to_supergal())
