# Disable debuginfo, since we package a stripped upstream binary.
%global debug_package %{nil}

# Disable autoprovides/requires for internal libraries
%global _privatelibs                 driveio
%global _privatelibs %{_privatelibs}|makemkv
%global _privatelibs %{_privatelibs}|mmdb
%global __provides_exclude ^lib(%{_privatelibs})\\.so.*
%global __requires_exclude ^lib(%{_privatelibs})\\.so.*

Name:           makemkv
Version:        1.14.7
Release:        0%{?dist}
Summary:        A format converter ("transcoder") for proprietary media

License:        Proprietary+GPLv2
URL:            https://www.makemkv.com/

Source0:        http://www.makemkv.com/download/%{name}-bin-%{version}.tar.gz
Source1:        http://www.makemkv.com/download/%{name}-oss-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(zlib)

ExclusiveArch:  i686 x86_64

%description
MakeMKV is your one-click solution to convert video that you own into free and
patents-unencumbered format that can be played everywhere. MakeMKV is a format
converter, otherwise called "transcoder". It converts the video clips from
proprietary (and usually encrypted) disc into a set of MKV files, preserving
most information but not changing it in any way. The MKV format can store
multiple video/audio tracks with all meta-information and preserve chapters.
There are many players that can play MKV files nearly on all platforms, and
there are tools to convert MKV files to many formats, including DVD and Blu-ray
discs.

Additionally MakeMKV can instantly stream decrypted video without intermediate
conversion to wide range of players, so you may watch Blu-ray and DVD discs
with your favorite player on your favorite OS or on your favorite device.

%prep
%setup -q -n %{name}-bin-%{version}
# Disable EULA prompt, because RPM install is effectively unattended, and
# let RPM determine DESTDIR/PREFIX.
sed -i -E \
  -e '/^(DESTDIR|PREFIX)=.*/d' \
  -e 's/install: tmp\/eula_accepted/install: /' \
  Makefile
%setup -q -T -D -b 1 -n %{name}-oss-%{version}


%build
%configure --enable-debug --enable-allcodecs
%make_build


%install
%make_install
cd ../%{name}-bin-%{version}
%make_install PREFIX=%{_prefix}


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%license License.txt
%{_bindir}/makemkv
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_libdir}/libdriveio.so*
%{_libdir}/libmakemkv.so*
%{_libdir}/libmmbd.so*

# Prebuilt binaries
%{_bindir}/makemkvcon
%{_datadir}/MakeMKV/appdata.tar
%{_datadir}/MakeMKV/blues.jar
%{_datadir}/MakeMKV/blues.policy


%changelog
* Tue Dec 10 2019 eric Mesa <ericsbinaryworld@gmail.com> - 1.14.7

* Sat Oct 5 2019 Eric Mesa <ericsbinaryworld@gmail.com> - 1.14.5
-Updated to latest release

* Sat Aug 31 2019 Eric Mesa <ericsbinaryworld@gmail.com> - 1.14.4
- Updated to latest release

* Sat Aug 31 2019 Eric Mesa <ericsbinaryworld@gmail.com> - 1.14.3-1
-Added zlib to buildrequires

* Fri Mar 15 2019 Ed Marshall <esm@logic.net> - 1.14.3-0
- Update to latest release.

* Tue Dec  5 2018 Ed Marshall <esm@logic.net> - 1.14.2-0
- Update to latest release.

* Tue Nov 13 2018 Ed Marshall <esm@logic.net> - 1.14.1-0
- Update to latest release.

* Sat Oct  6 2018 Ed Marshall <esm@logic.net> - 1.12.3-0
- Initial package.
