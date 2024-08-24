from typing import List, NewType

from plumbum.cmd import sudo, systemctl

services_list = NewType("services_list", List[str])

systemctl = sudo[systemctl]
enable_service = systemctl["enable"]
start_service = systemctl["start"]


def enable_service_list(services: services_list):
    for service in services:
        enable_service[service]()
        start_service[service]()
