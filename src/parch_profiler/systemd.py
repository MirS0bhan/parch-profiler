from typing import List, NewType

from plumbum.cmd import sudo, systemctl


systemctl = sudo[systemctl]
enable_service = systemctl["enable"]
start_service = systemctl["start"]


def enable_service_list(services: List[str]):
    for service in services:
        enable_service[service]()
        start_service[service]()
