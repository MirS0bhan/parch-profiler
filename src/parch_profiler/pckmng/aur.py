from plumbum.cmd import paru

from .base import PackageConfig, PackageManager


class ParuConf(PackageConfig):
    pass


# command
install_pck = paru["-S", "--noconfirm"]
list_pck = paru["-Qmq"]


class Paru(PackageManager):
    pckconf: ParuConf = ParuConf

    def install(self, pckconf: ParuConf):
        cmd = install_pck[pckconf.packages]
        return cmd()

    @classmethod
    def list(cls):
        cmd = list_pck
        return cls.pckconf(packages=cmd().splitlines())
