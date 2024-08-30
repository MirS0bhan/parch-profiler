from typing import List
from vlidt import BaseModel


class PackageConfig(BaseModel):
    packages: List[str]

