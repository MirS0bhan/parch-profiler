from plumbum.cmd import flatpak

from .base import PackageConfig, PackageManager


class FlatpakConf(PackageConfig):
    pass


# commands
install_pck = flatpak["install", "-y"]
list_pck = flatpak["list", "--app", "--columns=application"]


class Flatpak(PackageManager):
    pckconf: FlatpakConf = FlatpakConf

    def install(self):
        cmd = install_pck[self.pckconf.packages]
        return cmd()

    @classmethod
    def list(cls):
        cmd = list_pck
        return cls.pckconf(packages=cmd().splitlines())

