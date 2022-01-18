"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/plugins/stable/npe2_manifest_specification.html

Replace code below according to your needs.
"""
from __future__ import annotations


def faces_sample():
    from numpy.random import RandomState
    from sklearn.datasets import fetch_olivetti_faces

    rng = RandomState(0)

    faces, _ = fetch_olivetti_faces(return_X_y=True, shuffle=True, random_state=rng)

    return [(faces, {"name": "Olivetti Faces"})]
