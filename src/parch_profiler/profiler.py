from typing import Optional

from pydantic import BaseModel

from .pckmng import pckmng_gen, pckmng_ins, PACKAGES
from .systemd import services_list, enable_service_list


class Config(BaseModel):
    packages: PACKAGES
    systemd_services: Optional[services_list] = []


def install_config(conf: Config):
    pckmng_ins(conf.packages)  # installing packages

    if conf.systemd_services:
        enable_service_list(conf.systemd_services)


def generate_config(*pm_names):
    return Config(
        packages=pckmng_gen(*pm_names)
    )
