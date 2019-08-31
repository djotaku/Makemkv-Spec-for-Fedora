# Makemkv-Spec-for-Fedora
This is for the spec file to be able to great SRPMS and RPMs of Makemkv for Fedora

Building it requires some experience with building RPMs, but a high level summary:

    install the rpmdevtools and mock packages
    add yourself to the "mock" group, log out, log in again
    download the attached makemkv.spec file, make sure it's named correctly (ie. not makemkv.spec.txt)
    run "spectool -g makemkv.spec" to download the makemkv bin and oss tarballs
    as root, copy /etc/mock/fedora-28-x86_64.cfg to /etc/mock/makemkv.cfg and add stanzas for the RPMFusion free and non-free repositories (and their updates repos)
    as a user in the "mock" group, run "mock -r makemkv --sources=. --spec=makemkv.spec"
    if that works, copy the resulting .src.rpm from the results directory that it prints out to your current directory
    as a user in the "mock" group, run "mock -r makemkv --rebuild makemkv*.src.rpm"
    if *that* works, install the .x86_64.rpm from the results directory and enjoy

    
To help, here is the current set of RPMFusion stanzas (20190831):

[rpmfusion-free]
name=RPM Fusion for Fedora $releasever - Free
#baseurl=http://download1.rpmfusion.org/free/fedora/releases/$releasever/Everything/$basearch/os/
metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-$releasever&arch=$basearch
enabled=1
metadata_expire=14d
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever

[rpmfusion-nonfree]
name=RPM Fusion for Fedora $releasever - Nonfree
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/releases/$releasever/Everything/$basearch/os/
metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-$releasever&arch=$basearch
enabled=1
enabled_metadata=1
metadata_expire=14d
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever

[rpmfusion-nonfree-updates]
name=RPM Fusion for Fedora $releasever - Nonfree - Updates
#baseurl=http://download1.rpmfusion.org/nonfree/fedora/updates/$releasever/$basearch/
metalink=https://mirrors.rpmfusion.org/metalink?repo=nonfree-fedora-updates-released-$releasever&arch=$basearch
enabled=1
enabled_metadata=1
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-nonfree-fedora-$releasever


[rpmfusion-free-updates]
name=RPM Fusion for Fedora $releasever - Free - Updates
#baseurl=http://download1.rpmfusion.org/free/fedora/updates/$releasever/$basearch/
metalink=https://mirrors.rpmfusion.org/metalink?repo=free-fedora-updates-released-$releasever&arch=$basearch
enabled=1
enabled_metadata=1
type=rpm-md
gpgcheck=1
repo_gpgcheck=0
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-$releasever
