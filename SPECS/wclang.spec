%global commit0 816bdbbd68270ca92ff961780ccc15c47d6c2222
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global checkout 20150807git%{shortcommit0}

Name:           wclang
Version:        0.0.0
Release:        1.%{?checkout}%{?dist}
Summary:        MinGW wrapper for clang and clang++

License:        GPLv2
URL:            https://github.com/tpoechtrager/wclang
Source0:        https://github.com/tpoechtrager/%{name}/archive/%{commit0}.tar.gz/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  clang

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gcc


BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gcc

Requires:       clang
Requires:       mingw32-gcc
Requires:       mingw64-gcc

%description
Wclang is a tool which helps you to cross compile source code easily with
clang on Linux/Unix for Windows. Wclang is basically a wrapper for clang,
which allows you to directly target Windows. Wclang detects the target and
headers automatically and adds them to the clang invocation command.


%prep
%setup -qn %{name}-%{commit0}


%build
%cmake .
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/wclang
%{_bindir}/i686-w64-mingw32-clang
%{_bindir}/i686-w64-mingw32-clang++
%{_bindir}/x86_64-w64-mingw32-clang
%{_bindir}/x86_64-w64-mingw32-clang++


%changelog
* Fri Aug  7 2015 Marcel Wysocki <maci@satgnu.net> - 0.0.0-1.20150807git816bdbb
- Initial release
