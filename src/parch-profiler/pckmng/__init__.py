from typing import Dict, Type, List

from .base import PackageConfig, PackageManager

from .pacman import PacmanConf, Pacman
from .aur    import ParuConf, Paru

try:
    from .flatpak import FlatpakConf, Flatpak
except:
    pass  # TODO:  write a log for flatpak


package_managers = {
    pckmng.__class__.__name__.lower() : pckmng for pckmng in [
        Pacman(),
        Paru(),
        Flatpak()
    ]
}


def pckmng_gen(*pckmng_names: str) -> Dict[str, Type[PackageConfig]]:
    return {
        pm : package_managers[pm].list() for pm in pckmng_names
    }


def pckmng_ins(package_list: List[PackageConfig]):
    for package in package_list:
        pass


