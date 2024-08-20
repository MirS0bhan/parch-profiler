import toml
import subprocess
import os
import argparse

def run_subprocess(command, verbose=False):
    try:
        if verbose:
            result = subprocess.run(command)
        else:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print(f"Error running command: {' '.join(command)}")
        return result
    except subprocess.CalledProcessError as e:
        print(f"Subprocess error: {e}")

def install_generic_packages(command, packages):
    for package in packages:
        print(f"Installing package: {package}")
        run_subprocess(command + [package])

def install_packages(packages):
    install_generic_packages(["sudo", "pacman", "-S", "--noconfirm"], packages)

def install_aur_packages(aur_packages):
    install_generic_packages(["paru", "-S", "--noconfirm"], aur_packages)

def install_flatpak_packages(flatpak_packages):
    install_generic_packages(["flatpak", "install", "-y"], flatpak_packages)

def clone_config(config):
    for app, details in config.items():
        if app == "nvim":
            url = details['url']
            target_dir = os.path.expanduser("~/.config/nvim")
            print(f"Cloning Neovim config from {url} to {target_dir}")
            run_subprocess(["git", "clone", url, target_dir])

def enable_systemd_services(services):
    for service in services:
        print(f"Enabling systemd service: {service}")
        run_subprocess(["sudo", "systemctl", "enable", service])
        run_subprocess(["sudo", "systemctl", "start", service])

def check_toml(toml_file):
    try:
        toml.load(toml_file)
        print(f"{toml_file} is valid.")
    except toml.TomlDecodeError as e:
        print(f"Error in {toml_file}: {e}")

def generate_system_toml(output_file):
    # Get Pacman packages
    pacman_packages = subprocess.check_output(["pacman", "-Qeq"], text=True).splitlines()
    # Get AUR packages (using paru or yay, assuming paru here)
    aur_packages = subprocess.check_output(["paru", "-Qmq"], text=True).splitlines()
    # Get Flatpak packages
    flatpak_packages = subprocess.check_output(["flatpak", "list", "--app", "--columns=application"], text=True).splitlines()

    # Create TOML structure
    config = {
        "packages": {"packages": pacman_packages},
        "aur": {"aur_packages": aur_packages},
        "flatpak": {"flatpak_packages": flatpak_packages},
    }

    # Write to TOML file
    with open(output_file, "w") as f:
        toml.dump(config, f)

    print(f"Generated system package list in {output_file}")

    # Ask user to review and edit the file
    review = input("Do you want to review and edit the file? (y/n): ").strip().lower()

    if review == "y":
        editor = input("Choose an editor (vim/nano): ").strip().lower()
        if editor not in ["vim", "nano"]:
            print("Invalid editor choice. Skipping review.")
        else:
            subprocess.run([editor, output_file])

    print(f"TOML file saved as {output_file}")

def generate_file_toml(input_file, output_file):
    config = {
        "packages": {"packages": []},
        "aur": {"aur_packages": []},
        "flatpak": {"flatpak_packages": []},
    }

    with open(input_file, "r") as f:
        for line in f:
            key, value = line.split(":")
            key = key.strip()
            packages = [pkg.strip() for pkg in value.split(",")]

            if key == "packages":
                config["packages"]["packages"].extend(packages)
            elif key == "aur":
                config["aur"]["aur_packages"].extend(packages)
            elif key == "flatpak":
                config["flatpak"]["flatpak_packages"].extend(packages)

    with open(output_file, "w") as f:
        toml.dump(config, f)

    print(f"Generated TOML file from {input_file} and saved as {output_file}")

    # Ask user to review and edit the file
    review = input("Do you want to review and edit the file? (y/n): ").strip().lower()

    if review == "y":
        editor = input("Choose an editor (vim/nano): ").strip().lower()
        if editor not in ["vim", "nano"]:
            print("Invalid editor choice. Skipping review.")
        else:
            subprocess.run([editor, output_file])

    print(f"TOML file saved as {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Install packages and manage configurations from a TOML file.")
    parser.add_argument('--load', type=str, help='Path to the TOML file to load and install packages.')
    parser.add_argument('--check', type=str, help='Path to the TOML file to check for errors.')
    parser.add_argument('--generate-system', type=str, help='Generate a TOML file with system installed packages.')
    parser.add_argument('--generate-file', type=str, nargs=2, metavar=('input', 'output'),
                        help='Generate a TOML file from a text file. Provide input and output file paths.')

    args = parser.parse_args()

    if args.load:
        toml_file = args.load
        if os.path.exists(toml_file) and os.path.isfile(toml_file):
            config = toml.load(toml_file)
        else:
            print(f"TOML file {toml_file} does not exist or is not a valid file.")
            return

        # Install packages
        if 'packages' in config:
            install_packages(config['packages']['packages'])

        # Install AUR packages
        if 'aur' in config:
            install_aur_packages(config['aur']['aur_packages'])

        # Install Flatpak packages
        if 'flatpak' in config:
            install_flatpak_packages(config['flatpak']['flatpak_packages'])

        # Clone configuration
        if 'config' in config:
            clone_config(config['config'])

        # Enable systemd services
        if 'systemd' in config:
            enable_systemd_services(config['systemd']['systemd_services'])

    elif args.check:
        toml_file = args.check
        check_toml(toml_file)

    elif args.generate_system:
        output_file = args.generate_system
        generate_system_toml(output_file)

    elif args.generate_file:
        input_file, output_file = args.generate_file
        generate_file_toml(input_file, output_file)

    else:
        print("Please provide a valid argument.")

if __name__ == "__main__":
    main()
