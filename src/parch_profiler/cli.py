from pathlib import Path

import vlidt
import typer
import toml

from .profiler import install_config, generate_config, Config


app = typer.Typer()

CONFIG_FILE = "packages_config.toml"

from rich.console import Console


app = typer.Typer()
console = Console()

CONFIG_FILE = "config.toml"  # Define your default config file path


@app.command()
def gen(output: Path = typer.Option(Path(CONFIG_FILE), help="Path to save the generated config file")):
    """
    Generate a config file with the list of installed packages.
    """
    conf = generate_config()
    if vlidt.base.validate(conf):
        conf = vlidt.dump(conf)
        with open(output, "w") as f:
            toml.dump(conf, f)

    console.print(f"Config file generated at [bold green]{output}[/bold green] :boom:")


@app.command()
def apply(config: Path = typer.Option(Path(CONFIG_FILE), help="Path to the config file to apply")):
    """
    Apply the packages from the config file.
    """
    dd = toml.load(open(config, "r"))
    install_config(vlidt.load(Config, dd))
    console.print("[bold green]Packages applied successfully.[/bold green]")


@app.command()
def check(config: Path = typer.Option(Path(CONFIG_FILE), help="Path to the config file to validate")):
    """
    Validate the config file format.
    """
    data = toml.load(open(config, "r"))
    conf = vlidt.load(Config, data)
    vlidt.base.validate(conf)
    conf = vlidt.dump(conf)
    assert conf != data
    with open(config, "w") as f:
        toml.dump(conf, f)
    console.print("[bold green]Config file is valid.[/bold green] :white_check_mark:")


def main():
    app()


if __name__ == "__main__":
    main()
