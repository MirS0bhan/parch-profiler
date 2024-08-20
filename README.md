
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
python profiler.py --load config.toml
```

### **2. Validating a TOML Configuration**

Check if your TOML file is correctly formatted:

```bash
python profiler.py --check config.toml
```

### **3. Generating a System Package List**

Generate a TOML file listing all installed Pacman, AUR, and Flatpak packages:

```bash
python profiler.py --generate-system output.toml
```

### **4. Generating a TOML from a Text File**

Convert a simple text file into a TOML configuration:

```bash
python profiler.py --generate-file input.txt output.toml
```

### **5. Reviewing and Editing Generated TOML Files**

After generating a TOML file, you will be prompted to review and edit it using your preferred text editor (`vim` or `nano`).

---

## 🧰 **Sample `proto.toml` File**

Here’s a sample `proto.toml` file that you can use as a starting point for your configurations:

```toml
# Pacman packages to be installed
[packages]
packages = [
    "base-devel",
    "neovim",
    "git"
]

# AUR packages to be installed
[aur]
aur_packages = [
    "google-chrome",
    "paru-bin"
]

# Flatpak packages to be installed
[flatpak]
flatpak_packages = [
    "com.spotify.Client",
    "org.videolan.VLC"
]

# Configuration repositories to clone
[config]
nvim = { url = "https://github.com/yourusername/nvim-config.git" }

# Systemd services to enable and start
[systemd]
systemd_services = [
    "docker.service",
    "nginx.service"
]
```

---

## 📄 **Sample `input.txt` for TOML Generation**

If you prefer to start from a simple text file, here’s how your `input.txt` might look:

```text
packages: base-devel, neovim, git
aur: google-chrome, paru-bin
flatpak: com.spotify.Client, org.videolan.VLC
```

---

## 🛠️ **Installation**

To use Parch-Profiler on Parch Linux, clone the repository and ensure you have Python installed on your system:

```bash
git clone https://git.parchlinux.com/applications/parch-profiler.git
cd parch-profiler
python profiler.py --help
```

---

## ✨ **Contributing**

We welcome contributions! Please feel free to submit a Merge Request or open an Issue on GitLab.

---

## 📜 **License**

This project is licensed under the GPL-3 License - see the [LICENSE](./LICENSE) file for details.

---

## 🛠️ **Requirements**

- **Python 3.x**
- **Parch Linux**
- **Pacman, paru, flatpak**

---

## 📧 **Support**

For any issues or feature requests, please reach out through the GitLab repository.


