import os
import json

arch_dependencies = ['base-devel']
arch_packages = ['xorg', 'xorg-server', 'xorg-xinit', 'zsh', 'sddm', 'neofetch', 'nitrogen', 'iw', 'light', 'i3-gaps', 'dash', 'dunst', 'compton', 'lshw', 'rofi', 'termite', 'feh', 'python-dbus', 'python-pip', 'wget', 'xterm', 'xrandr', 'pulseaudio', 'pulseaudio-alsa', 'alsa-utils', 'firefox', 'openssh', 'git', 'dmidecode', 'ranger', 'scrot', 'khal', 'mpd', 'ncmpcpp', 'p7zip', 'redshift', 'vdirsyncer', 'mopidy', 'wireguard-tools', 'wireguard-arch', 'keepassxc', 'htop', 'thunar', 'openbox', 'obconf', 'gimp', 'libreoffice-still', 'picom']
aur_packages = ['polybar', 'compton-tyrone-git', 'yay', 'cava', 'dropbox', 'ttf-google-sans', 'pipes.sh']
yay_packages = ['mopidy-spotify', 'gotop']
python_packages = ['requests', 'bs4', 'html5lib', 'tqdm', 'wheel', 'mopidy-iris']
ttf_fonts = ['ttf-hack', 'ttf-font-awesome', 'ttf-fira-code']
otf_fonts = ['otf-font-awesome']

pwd = os.getcwd()
json_data_path = f'{pwd}/json_data'

def generator(filename, items):
    """
    """
    data = []

    for item in items:
        d = {
            'name': item,
            'url': '',
            'description': ''
        }

        data.append(d)

    with open(f"{json_data_path}/{filename}.json", 'w') as output:
        json.dump(data, output, indent=4)

def main():
    """
    """
    generator('arch_dependencies', arch_dependencies)
    generator('arch_packages', arch_packages)
    generator('aur_packages', aur_packages)
    generator('yay_packages', yay_packages)
    generator('python_packages', python_packages)
    generator('ttf_fonts', ttf_fonts)
    generator('otf_fonts', otf_fonts)

if __name__ == "__main__":
    main()
