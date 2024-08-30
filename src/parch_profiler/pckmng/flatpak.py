from plumbum.cmd import flatpak

from .base import PackageConfig


class FlatpakConf(PackageConfig):
    pass


# commands
install_pck = flatpak["install", "-y"]
list_pck = flatpak["list", "--app", "--columns=application"]


def install(self):
    cmd = install_pck[self.pckconf.packages]
    return cmd()


def pkg_list():
    cmd = list_pck
    return FlatpakConf(packages=cmd().splitlines())
