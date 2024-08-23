from typing import Type, List
from abc import ABC, abstractmethod
from pydantic import BaseModel


class PackageConfig(BaseModel):
    packages: List[str]


class PackageManager(ABC):
    pckconf: Type[PackageConfig] = None

    # def __init__(self, pckconf: PackageConfig):
    #     if isinstance(pckconf, self.pckconf):
    #         self.pckconf = pckconf

    @abstractmethod
    def install(self):
        raise NotImplemented()

    @property
    def list(self):
        raise NotImplemented()
