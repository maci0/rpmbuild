Name:           keepassx2
Version:        2.0.alpha5
Release:        1%{?dist}
Summary:        Cross Platform Password Manager

License:        GPL-2.0 and LGPL-2.1 and LGPL-3.0+
URL:            http://www.keepassx.org/
Source0:        keepassx-2.0-alpha5.tar.gz

BuildRequires:  cmake
BuildRequires:  qt-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libXtst-devel
BuildRequires:  desktop-file-utils

Obsoletes:       keepassx

%description
A free/open-source password manager or safe which helps you to
manage your passwords in a secure way. You can put all your passwords in one
database, which is locked with one master key or a key-disk. So you only have
to remember one single master password or insert the key-disk to unlock the
whole database. The databases are encrypted using the best and most secure
encryption algorithms currently known (AES and Twofish).

%prep
%setup -q -n keepassx-2.0-alpha5

%build
%cmake .
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/keepassx
%{_datadir}/keepassx
%{_libdir}/keepassx
%{_datadir}/icons/hicolor
%{_datadir}/applications/keepassx.desktop

%changelog
* Wed Jan 29 2014 maci <maci@satgnu.net>
- initial spec file
