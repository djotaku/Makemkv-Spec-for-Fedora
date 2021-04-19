# MakeMKV-Spec-for-Fedora

This is for the spec file to be able to create SRPMs and RPMs of MakeMKV for Fedora. The MakeMKV RPMs are built with [mock](https://github.com/rpm-software-management/mock/).

- Install the rpmdevtools and mock packages
- Add yourself to the "mock" group, log out, log in again
- Setup [RPM Fusion](https://rpmfusion.org/Configuration) repository

  ```bash
  sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
  ```

- Setup rpmfusion for mock

  ```bash
  sudo dnf install mock-rpmfusion-free.noarch mock-rpmfusion-nonfree.noarch
  ```

- Clone this repo and cd into the cloned directory

  ```bash
  git clone https://github.com/djotaku/Makemkv-Spec-for-Fedora.git
  cd Makemkv-Spec-for-Fedora
  ```

- Build and Install the RPM package

  This will also pull the current beta key from the MakeMKV website and write it to the configuration file for registration.

  ```bash
  chmod +x update.sh
  ./update.sh
  ```

## Updating MakeMKV

For future updates of MakeMKV, run the update script (provided this repository was updated for the updated version).

 ```bash
 ./update.sh
 ```

## Updating the Beta Key

In case the Key runs out before there is a new update, you can also disable building and installing the RPM to only update the key by using the `--nobuild` argument

 ```bash
 ./update.sh --nobuild
 ```

## Deprecated steps

**Note:** These steps are ***not*** required anymore, as they have been integrated into the aforementioned update script. These are purely for reference in case you run into issues with the script (change version numbers accordingly).

- Download the makemkv bin and oss tarballs

  ```bash
  spectool -g makemkv.spec
  ```

- Build the RPM packages (as a user in the "mock" group)

  ```bash
  mock -r fedora-33-x86_64-rpmfusion_nonfree --sources=. --spec=makemkv.spec
  ```

- Copy the resulting .rpm from the results directory that it prints out to your current directory

  ```bash
  cp /var/lib/mock/fedora-33-x86_64/result/makemkv-1.16.3-1.fc33.*.rpm .
  ```

- Install the .x86_64.rpm from the results directory and enjoy

  ```bash
  sudo dnf install makemkv-1.16.3-1.fc33.x86_64.rpm
  ```
