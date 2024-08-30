from plumbum.cmd import sudo, pacman

from .base import PackageConfig


class PacmanConf(PackageConfig):
    pass


# commands
install_pck = sudo[pacman["-S", "--noconfirm"]]
list_pck = pacman["-Qeq"]


def install(pkg_conf: PacmanConf):
    cmd = install_pck[pkg_conf.packages]
    return cmd()


def pkg_list() -> PacmanConf:
    cmd = list_pck
    return PacmanConf(packages=cmd().splitlines())
