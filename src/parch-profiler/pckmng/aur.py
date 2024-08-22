from plumbum.cmd import sudo, paru

from .base import PackageConfig, PackageManager


class ParuConf(PackageConfig):
    pm: str = 'paru'


class Paru(PackageManager):
    pckconf: ParuConf = ParuConf

    def install(self):
        cmd = sudo[paru['-Syu', self.pckconf.packages]]
        cmd()

    def list(self):
        cmd = paru["-Qeq"]
        return ParuConf(packages=cmd().splitlines())
