from plumbum.cmd import paru

from .base import PackageConfig


class ParuConf(PackageConfig):
    pass


# command
install_pck = paru["-S", "--noconfirm"]
list_pck = paru["-Qmq"]


def install(pkg_conf: ParuConf):
    cmd = install_pck[pkg_conf.packages]
    return cmd()


def pkg_list():
    cmd = list_pck
    return ParuConf(packages=cmd().splitlines())
