#!/usr/bin/env python

import os, sys
import json
import subprocess
from datetime import datetime

from logger import Logger

log = Logger(__file__)

__version__ = "0.1.0"

pwd = os.getcwd()
config = f'{pwd}/.config'
buildhere = f'{pwd}/buildhere'
json_data_path = f'{pwd}/json_data'
scripts_path = f'{pwd}/scripts'

def get_config_locat():
    """
    Scans the .config directory and retrieves the folders name in a list
    """
    config_locat = []

    try:
        config_locat = [f.name for f in os.scandir(config) if f.is_dir()]
    except Exception as ex:
        log.error(ex)
        print(f"Error while scanning the folder '{config}'.")

    return config_locat

config_locat = get_config_locat()

def run(cmd):
    """
    Runs a command by using subprocess system and and interactive shell
    """
    return subprocess.call(cmd, shell=True)

def run_script(script):
    """
    Runs a custom script
    """
    if is_null_or_empty(script):
        print(f"Script not specified.")
        return

    script_path = os.path.join(scripts_path, script)

    if not os.path.exists(script_path):
        print(f"The script '{script_path}' could not be found.")
        return

    shell = 'dash' if script.endswith('.dash') else 'sh'

    run(f'{shell} {script_path}')

def install_arch_packages():
    """
    Installs packages using pacman package manager
    """
    arch_packages = get_packages("arch_packages")

    if is_null_or_empty(arch_packages):
        print("No packages found.")
        return

    packages = " ".join(arch_packages)

    print('Installing packages from ARCH repositories')
    run(f'sudo pacman -S {packages} --noconfirm')

def install_arch_deps():
    """
    Installs those dependencies needed by Arch Linux
    """
    arch_dependencies = get_packages("arch_dependencies")

    if is_null_or_empty(arch_dependencies):
        print(f"No dependencies found.")
        return

    deps = " ".join(arch_dependencies)

    print('Installing AUR dependencies')
    run(f'sudo pacman -S {deps} --noconfirm')

def install_aur_packages():
    """
    Installs packages from the AUR system
    """
    aur_packages = get_packages("aur_packages")

    if is_null_or_empty(aur_packages):
        print(f"No packages found.")
        return

    print("Installing packages from AUR")

    for package in aur_packages:
        print(f"Installing package {package}...")

        run(f"git clone https://aur.archlinux.org/{package} {buildhere}")
        run(f"cd {buildhere} && makepkg -si")
        run(f"cd {pwd}/ && rm -rf {buildhere}")

def install_yay_packages():
    """
    Installs packages using YAY package manager
    """
    yay_packages = get_packages("yay_packages")

    if is_null_or_empty(yay_packages):
        print(f"No packages found.")
        return

    yay = " ".join(yay_packages)

    print('Installing YAY packages')
    run(f'sudo yay -S {yay}')

def install_python_packages():
    """
    Installs all required python packages
    """
    python_packages = get_packages("python_packages")

    if is_null_or_empty(python_packages):
        print(f"No packages found.")
        return

    packages = " ".join(python_packages)

    print("Installing Python packages")
    run(f"sudo python3 -m pip install {packages}")

def install_zsh():
    """
    Installs the oh-my-zsh shell using a custom script
    """
    print("Installing oh-my-zsh")
    run('sh -c "$(wget -O- https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"')

def install_ttf_fonts():
    """
    Installs defined TTF fonts
    """
    ttf_fonts = get_packages("ttf_fonts")

    if is_null_or_empty(ttf_fonts):
        print(f"No TTF fonts found.")
        return

    packages = " ".join(ttf_fonts)

    print("Installing TTF Fonts")
    run(f"pacman -S {packages} --noconfirm")

def install_otf_fonts():
    """
    Installs defined OTF fonts
    """
    otf_fonts = get_packages("otf_fonts")

    if is_null_or_empty(otf_fonts):
        print(f"No TTF fonts found.")
        return

    packages = " ".join(otf_fonts)

    print("Installing OTF Fonts")
    run(f"pacman -S {packages} --noconfirm")

def set_resolution(display, resolution):
    """
    Sets the resolution for a given display/monitor using xrandr
    """
    if is_null_or_empty(resolution):
        print("Resolution param was not set.")
        return

    if 'x' not in resolution:
        print("Invalid resolution format.")
        return

    run(f'xrandr --output {display} --mode {resolution}')

def cleanup():
    """
    Removes the current configuration by deleting the appropiate folders and files.
    """
    print("Removing existing configuration")

    for package in config_locat:
        run(f'rm -rf ~/.config/{package}')

    # Folders
    run('rm -rf ~/.bin')
    run('rm -rf ~/.fonts')
    run('rm -rf ~/.sysd')
    run('rm -rf ~/.themes')
    run('rm -rf ~/.config/gtk-2.0')
    run('rm -rf ~/.config/gtk-3.0')

    # Files
    run('rm -rf ~/.bash_profile')
    run('rm -rf ~/.xinitrc')
    run('rm -rf ~/.Xresources')
    run('rm -rf ~/.oh-my-zsh') # Required to reinstall oh-my-zsh
    run('rm -rf ~/.zprofile')
    run('rm -rf ~/.zshrc')

def copy_config():
    """
    Copies the configuration files/folders
    """
    print("Copying configuration files")

    for package in config_locat:
        run(f'cp -R {pwd}/.config/{package} ~/.config/{package}')

    # Folders
    run(f'cp -R {pwd}/.bin ~/.bin')
    run(f'cp -R {pwd}/.fonts ~/.fonts')
    run(f'cp -R {pwd}/.sysd ~/.sysd')
    run(f'cp -R {pwd}/.themes ~/.themes')
    run(f'cp -R {pwd}/.config/gtk-2.0 ~/.config/gtk-2.0')
    run(f'cp -R {pwd}/.config/gtk-3.0 ~/.config/gtk-3.0')

    # Files
    run(f'cp {pwd}/.bash_profile ~/.bash_profile')
    run(f'cp {pwd}/.xinitrc ~/.xinitrc')
    run(f'cp {pwd}/.Xresources ~/.Xresources')
    run(f'cp {pwd}/.zprofile ~/.zprofile')
    run(f'cp {pwd}/.zshrc ~/.zshrc')
    run(f'cp {pwd}/sudoers.lecture /etc/sudoers.lecture')

def symlink():
    """
    Creates symboling links for files/folders
    """
    print("Symlink config files")

    for package in config_locat:
        run(f'ln -s ~/dotfiles/.config/{package} ~/.config/')

    run('ln -s ~/dotfiles/.fonts ~/.fonts')
    run('ln -s ~/dotfiles/.xinitrc ~/.xinitrc')
    run('ln -s ~/dotfiles/.bin ~/.bin')
    run('ln -s ~/dotfiles/.themes/ ~/.themes')
    run('ln -s ~/dotfiles/.config/gtk-3.0/gtk.css ~/.config/gtk-3.0/gtk.css')
    run('ln -s ~/dotfiles/.zshrc/ ~/.zshrc')

def is_null_or_empty(obj):
    """
    Checks if a given object is either Null, empty or a length of 0
    """
    validations = []

    validations.append(obj is None)
    validations.append(obj == "")

    if isinstance(obj, list) or isinstance(obj, dict):
        validations.append(len(obj) == 0)

    return any(validations)

def get_packages(filename):
    """
    Returns a list containing the names of the packages given from a json file
    """
    packages = []

    json_data = read_json_file(f"{json_data_path}/{filename}.json")

    if not is_null_or_empty(json_data):
        packages = [item['name'] for item in json_data if not is_null_or_empty(item['name'])]

    return packages

def read_json_file(path):
    """
    Reads a json file and returns the data
    """
    data = None

    if is_null_or_empty(path):
        print(f"Path not specified.")
        return data

    if not os.path.exists(path):
        print(f"Path '{path}' does not exists.")
        return data

    try:
        with open(path) as f:
            data = json.load(f)
    except Exception as ex:
        log.error(ex)
        print(f"Error processing the file.")

    return data

def main():
    """
    """
    # Remove previous configuration
    cleanup()

    # Start installation
    install_arch_packages()
    install_arch_deps()
    install_aur_packages()
    install_yay_packages()
    install_python_packages()
    install_ttf_fonts()
    install_otf_fonts()

    # Install zsh at the end
    # because it enters automatically
    # and skips the rest of the installation
    install_zsh()

    # Exit from zsh
    run('exit')

    # Add symlinks to packages
    #symlink()

    # Copy configuration
    copy_config()

    print("Finished! Don't forget to enable your theme and logout.")

if __name__ == '__main__':
    main()
