from ..pckmng import pacman, aur, flatpak

from .base import PackageConfig


_package_managers = {
    pkgmgr.__name__.split('.')[-1] : pkgmgr for pkgmgr in [
        pacman,
        aur,
        flatpak
    ]
}


def package_manager(name: str):
    return _package_managers[name]


def pckmng_gen(*packages: str):
    return {
        name : package_manager(name).pkg_list() for name in packages
    }


def pckmng_ins(packages):
    for name, config in packages.items():
        pc = package_manager(name)
        pc.install(config)
