"""Absolute paths to the URDFs shipped inside the package.

One function rather than the expression inline at each call site: an integrator that stages its
own copies of these files patches this name and every lookup follows, which an expression spread
over three modules does not allow.
"""
from importlib.resources import files


def asset_path(name: str) -> str:
    """Return the absolute path of a file in the package's assets directory."""
    return str(files('gym_pybullet_drones') / 'assets' / name)
