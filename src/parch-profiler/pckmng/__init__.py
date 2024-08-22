from .base import PackageConfig, PackageManager

from .pacman import PacmanConf, Pacman
from .aur    import ParuConf, Paru

try:
    from .flatpak import FlatpakConf, Flatpak
except:
    pass  # TODO:  write a log for flatpak



