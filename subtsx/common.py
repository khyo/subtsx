from pathlib import Path
from typing import Optional, Any
import typing



class vars:
    ESBUILD_VERSION = "0.19.4"
    """ The one-true esbuild version (aka default version) """
    lib_dir = Path(__file__).parent
    """ Path to the subelectron library files """
