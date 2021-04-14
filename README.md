# Makemkv-Spec-for-Fedora

This is for the spec file to be able to create SRPMS and RPMs of Makemkv for Fedora. The makemkv rpms are build with mock.

- Install the rpmdevtools and mock packages
- Add yourself to the "mock" group, log out, log in again
- Setup rpmfusion repo (acc. <https://rpmfusion.org/Configuration>)

  ```bash
  sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
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
  cp /var/lib/mock/fedora-31-x86_64/result/makemkv-1.14.7-0.fc31.*.rpm .
  ```

- Install the .x86_64.rpm from the results directory and enjoy

  ```bash
  sudo dnf install makemkv-1.14.7-0.fc31.x86_64.rpm
  ```
