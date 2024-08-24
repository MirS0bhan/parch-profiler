from typing import Dict, Type

from pydantic import BaseModel

from pckmng import PackageConfig, pckmng_gen, pckmng_ins, PACKAGES


class Config(BaseModel):
    packages: PACKAGES


def install_config(conf: Config):
    pckmng_ins(conf.packages)


def generate_config(*pm_names):
    return Config(
        packages=pckmng_gen(*pm_names)
    )
