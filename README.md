### 📦 **Parch-Profiler**

Parch-Profiler is a powerful Python-based utility designed specifically for Parch Linux. It simplifies the management of system packages and configurations by allowing you to generate, validate, and install packages—including AUR and Flatpak—using a structured TOML configuration file.

---

## 🚀 **Features**

- **Package Installation:**
  - Install packages using Pacman, AUR (via `paru`), and Flatpak from a single TOML file.

- **Configuration Management:**
  - Clone configuration files, such as Neovim setups, directly from Git repositories.

- **Systemd Service Management:**
  - Enable and start systemd services as specified in the TOML configuration.

- **TOML Validation:**
  - Validate your TOML files to ensure they are correctly formatted.

- **Package List Generation:**
  - Automatically generate TOML files listing all installed Pacman, AUR, and Flatpak packages.

- **File-based TOML Generation:**
  - Convert simple text files listing packages into structured TOML files.

---

## 📄 **Usage**

### **1. Loading a TOML Configuration**

To install packages, clone configurations, and enable services:

```bash
parch-profiler apply --config config.toml
```

### **2. Validating a TOML Configuration**

Check if your TOML file is correctly formatted:

```bash
parch-profiler check config.toml
```

### **3. Generating a System Package List**

Generate a TOML file listing all installed Pacman, AUR, and Flatpak packages:

```bash
parch-profiler gen
```

## 🧰 **Sample `proto.toml` File**

Here’s a sample `proto.toml` file that you can use as a starting point for your configurations:

```toml
# Pacman packages to be installed
[packages.pacman]
packages = [
    "base-devel",
    "neovim",
    "git"
]

# AUR packages to be installed
[packages.paru]
packages = [
    "google-chrome",
    "paru-bin"
]

# Flatpak packages to be installed
[packages.flatpak]
packages = [
    "com.spotify.Client",
    "org.videolan.VLC"
]

# Systemd services to enable and start
[systemd]
systemd_services = [
    "docker.service",
    "nginx.service"
]
```

---

## 🛠️ **Installation**

To use Parch-Profiler on Parch Linux, clone the repository and ensure you have Python installed on your system:

```bash
git clone https://github.com/MirS0bhan/parch-profiler.git
python parch-profiler --help
```
OR
```bash
sudo pacman -S parch-profiler
parch-profiler --help
```

---

## ✨ **Contributing**

We welcome contributions! Please feel free to submit a Merge Request or open an Issue on GitLab.

---

## 📜 **License**

This project is licensed under the GPL-3 License - see the [LICENSE](./LICENSE) file for details.

---

## 🛠️ **Requirements**

- **Python ^3.8**
- **Parch Linux**
- **Pacman, paru, flatpak**

---

## 📧 **Support**

For any issues or feature requests, please reach out through the GitLab repository.


