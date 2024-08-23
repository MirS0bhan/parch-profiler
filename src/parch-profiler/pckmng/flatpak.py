from plumbum.cmd import flatpak

from .base import PackageConfig, PackageManager


class FlatpakConf(PackageConfig):
    pass


class Flatpak(PackageManager):
    pckconf: FlatpakConf = FlatpakConf

    def install(self):
        cmd = flatpak["install", "-y", self.pckconf.packages]
        return cmd()

    def list(self):
        cmd = flatpak["list", "--app", "--columns=application"]
        return FlatpakConf(packages=cmd().splitlines())

