from pathlib import Path

import typer
import toml

from .profiler import install_config, generate_config, Config
from .pckmng import _package_managers

app = typer.Typer()

CONFIG_FILE = "packages_config.toml"


@app.command()
def gen(output: Path = typer.Option(Path(CONFIG_FILE), help="Path to save the generated config file")):
    """
    Generate a config file with the list of installed packages.
    """
    dd = generate_config(*list(_package_managers.keys())).model_dump()
    toml.dump(dd, open(output, "w"))

    typer.echo(f"Config file generated at {output}")


@app.command()
def apply(config: Path = typer.Option(Path(CONFIG_FILE), help="Path to the config file to apply")):
    """
    Apply the packages from the config file.
    """
    dd = toml.load(open(config, "r"))
    install_config(Config(**dd))
    typer.echo("Packages applied successfully.")


@app.command()
def check(config: Path = typer.Option(Path(CONFIG_FILE), help="Path to the config file to validate")):
    """
    Validate the config file format.
    """
    # Implementation goes here
    typer.echo("Config file is valid.")


def main():
    app()


if __name__ == "__main__":
    main()
