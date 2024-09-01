from ..pckmng import pacman, aur, flatpak

from .base import PackageConfig
from vlidt import BaseModel


_package_managers = {
    pkgmgr.__name__.split('.')[-1] : pkgmgr for pkgmgr in [
        pacman,
        aur,
        flatpak
    ]
}


class PackageManager(BaseModel):
    pacman: pacman.PacmanConf
    aur: aur.ParuConf
    flatpak: flatpak.FlatpakConf


def package_manager(name: str):
    return _package_managers[name]


def pckmng_gen():
    return PackageManager(
        pacman.pkg_list(),
        aur.pkg_list(),
        flatpak.pkg_list()
    )


def pckmng_ins(packages):
    for name, config in packages.items():
        pc = package_manager(name)
        pc.install(config)
