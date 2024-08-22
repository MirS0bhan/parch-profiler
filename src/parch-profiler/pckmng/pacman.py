from plumbum.cmd import sudo, pacman

from .base import PackageConfig, PackageManager


class PacmanConf(PackageConfig):
    pm: str = 'pacman'


class Pacman(PackageManager):
    pckconf: PacmanConf = PacmanConf

    def install(self):
        cmd = sudo[pacman['-Syu', self.pckconf.packages]]
        cmd()

    def list(self):
        cmd = pacman["-Qeq"]
        return PacmanConf(packages=cmd().splitlines())
