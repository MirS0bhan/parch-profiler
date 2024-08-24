from typing import Type, List, NewType, Dict
from abc import ABC, abstractmethod
from pydantic import BaseModel


class PackageConfig(BaseModel):
    packages: List[str] = []


class PackageManager(ABC):
    pckconf: Type[PackageConfig] = None

    def __init__(self):
        pass

    @abstractmethod
    def install(self, packages: PackageConfig):
        raise NotImplemented()

    @classmethod
    @abstractmethod
    def list(cls) -> PackageConfig:
        raise NotImplemented()


PACKAGES = NewType("PACKAGES", Dict[str, PackageConfig])
