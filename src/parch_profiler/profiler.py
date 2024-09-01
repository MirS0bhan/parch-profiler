from typing import Optional, Dict, Type, List

from vlidt import BaseModel

from .pckmng import pckmng_gen, pckmng_ins, PackageManager
from .systemd import enable_service_list
from .nvim import nvim_upstream, NvimConfig


class Config(BaseModel):
    packages: PackageManager
    systemd_services: Optional[List[str]] = None
    nvim: NvimConfig = None


def install_config(conf: Config):
    pckmng_ins(conf.packages)  # installing packages

    if conf.systemd_services:
        enable_service_list(conf.systemd_services)


def generate_config():
    return Config(
        pckmng_gen(),
        nvim=nvim_upstream()
    )
