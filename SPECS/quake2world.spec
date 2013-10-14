%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

Name:           quake2world
Version:        0.0.1
Release:        3%{?dist}
Summary:        A Free FPS game.

Group:          Amusements/Games
License:        GPL
URL:            http://quake2world.net
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  SDL-devel SDL_image-devel SDL_mixer-devel libcurl-devel libjpeg-devel zlib-devel physfs-devel glib2-devel wget openssh-clients libtool

%description
Quake2World is an unsupported, unofficial, multiplayer-only iteration of id Software's Quake II. 
It aims to blend the very best aspects of the entire Quake series to deliver an enjoyable 
FPS experience in a free to download, stand-alone game.

%prep
%setup -q -n %{name}-%{version}
wget https://github.com/jdolan/quake2world/archive/master.zip -O master.zip
unzip master.zip
cd quake2world-*
libtoolize
autoreconf -i

%build
cd quake2world-*
%configure
make %{?_smp_mflags}

%install
cd quake2world-*
cd linux
make release
make release-image

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Apr 23 2013 Marcel Wysocki <maci@satgnu.net> - 0.0.1-3
- added physfs dep
- added glib2 dep
- added wget dep
- use github instead of svn
- remove subversion dep

* Sun Jul 29 2012 Marcel Wysocki <maci@satgnu.net> 0.0.1-2
- Remove packaging
- Update dependencies
- Upload to quake2world.net

* Tue Jul 17 2007 maci <maci@satgnu.net> 0.0.1-1
- Initial release

