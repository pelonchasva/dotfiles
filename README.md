# dotfiles

This repository contains my configuration for my Arch Linux distro, which I use primarly on a VM until it is stable to install on a real machine.

## Dependencies

* Python >= 3.6
* pip

## Installation

Clone this repo

```bash
git clone && cd ~/repos/dotfiles
```

As an additional step, in order to avoid typing your user password everytime when using sudo, add a temporary environment variable to provide this value when running the installer

```bash
env SUDO_PASSWORD=<your password>
```

Run the `generator.py` script first so the json files are up to date

```bash
python generator.py
```

Finally, run the installer script

```bash
python installer.py
```

## Packages

## References

<https://audreyxie.com/2020/sudowoodo-reminding-you-to-be-careful-when-using-sudo/>

## License
