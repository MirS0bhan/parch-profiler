from typing import Dict, Type, List

from .base import PackageConfig, PackageManager, PACKAGES

from .pacman import PacmanConf, Pacman
from .aur    import ParuConf, Paru

try:
    from .flatpak import FlatpakConf, Flatpak
except:
    pass  # TODO:  write a log for flatpak


_package_managers = {
    pckmng.__class__.__name__.lower() : pckmng for pckmng in [
        Pacman(),
        Paru(),
        Flatpak()
    ]
}


def package_manager(name: str) -> PackageManager:
    return _package_managers[name]


def pckmng_gen(*packages: str) -> PACKAGES:
    return {
        name : package_manager(name).list() for name in packages
    }


def pckmng_ins(packages: PACKAGES):
    for name, config in packages.items():
        pc: PackageManager = package_manager(name)
        pc.install(config)
