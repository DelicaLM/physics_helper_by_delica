from .physics_funcs import *
from importlib.metadata import version, PackageNotFoundError

__version__ = "unknown"
try:
    __version__ = version("physics_helper_by_delica")
except PackageNotFoundError:
    pass

__all__ = ["physics_funcs.py"]
