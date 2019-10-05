# Makemkv-Spec-for-Fedora
This is for the spec file to be able to great SRPMS and RPMs of Makemkv for Fedora

Building it requires some experience with building RPMs, but a high level summary:

 - install the rpmdevtools and mock packages
 - add yourself to the "mock" group, log out, log in again
 - copy the spec file from this repo into the directory you want to work in.
 - run "spectool -g makemkv.spec" to download the makemkv bin and oss tarballs
 - as root, copy /etc/mock/fedora-N-x86_64.cfg (where N is the version of Fedora that you want to build an RPM for) to /etc/mock/makemkv.cfg and add stanzas for the RPMFusion free and non-free repositories (and their updates repos). You only have to do this step once per Fedora version that you want to target. You don't need to do it with each new verion of MakeMKV.
 - as a user in the "mock" group, run "mock -r makemkv --sources=. --spec=makemkv.spec"
  - if that works, copy the resulting .rpm from the results directory that it prints out to your current directory
  - install the .x86_64.rpm from the results directory and enjoy

    
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

Also, know that if you're doing mock for a version of Fedora different from the machine on which you're running it, you will need to manually import RPMFusion's keys for that version or it will fail on the mock -r step.
