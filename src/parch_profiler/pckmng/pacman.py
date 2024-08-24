from plumbum.cmd import sudo, pacman

from .base import PackageConfig, PackageManager


class PacmanConf(PackageConfig):
    pass


# commands
install_pck = sudo[pacman["-S", "--noconfirm"]]
list_pck = pacman["-Qeq"]


class Pacman(PackageManager):
    pckconf: PacmanConf = PacmanConf

    def install(self, pckconf: PacmanConf):
        cmd = install_pck[pckconf.packages]
        return cmd()

    @classmethod
    def list(cls) -> PacmanConf:
        cmd = list_pck
        return cls.pckconf(packages=cmd().splitlines())
