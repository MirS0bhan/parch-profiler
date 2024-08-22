from typing import List

import toml
from pydantic import BaseModel

from .pckmng import PackageConfig

class Config(BaseModel):
    packages: List[PackageConfig]


class Profiler:
    pass