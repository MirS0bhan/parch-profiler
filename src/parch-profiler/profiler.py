from typing import Dict

from pydantic import BaseModel

from pckmng import PackageConfig, pckmng_gen


class Config(BaseModel):
    packages: Dict[str, PackageConfig]


def install_config(conf: Config):
    pass


def generate_config(*pm_names):
    return Config(
        packages=pckmng_gen(*pm_names)
    ).model_dump()
