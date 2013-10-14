%{?mingw_package_header}

Name:           mingw-physfs
Version:        2.0.3
Release:        4%{?dist}
Summary:        MinGW compiled physfs library to provide abstract access to various archives

License:        zlib
Group:          Development/Libraries
URL:            http://www.icculus.org/physfs/
Source0:        http://www.icculus.org/physfs/downloads/physfs-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  libtool


BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-readline


BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-readline


%description
MinGW compiled PhysicsFS, a library to provide abstract access 
to various archives. It is intended for use in video games, and the 
design was somewhat inspired by Quake 3's file subsystem. 
The programmer defines a "write directory" on the physical filesystem. 
No file writing done through the PhysicsFS API can leave that 
write directory, for security. 
For example, an embedded scripting language cannot write outside of 
this path if it uses PhysFS for all of its I/O, which means that 
untrusted scripts can run more safely. Symbolic links can be disabled 
as well, for added safety. For file reading, the programmer lists 
directories and archives that form a "search path". 
Once the search path is defined, it becomes a single, 
transparent hierarchical filesystem. 
This makes for easy access to ZIP files in the same way as you access 
a file directly on the disk, and it makes it easy to ship a new archive 
that will override a previous archive on a per-file basis. 
Finally, PhysicsFS gives you platform-abstracted means to determine 
if CD-ROMs are available, the user's home directory, where in the 
real filesystem your program is running, etc.

# Win32
%package -n mingw32-physfs
Summary:       MinGW compiled physfs library for the Win32 target

%description -n mingw32-physfs
MinGW compiled PhysicsFS, a library to provide abstract access 
to various archives. It is intended for use in video games, and the 
design was somewhat inspired by Quake 3's file subsystem. 
The programmer defines a "write directory" on the physical filesystem. 
No file writing done through the PhysicsFS API can leave that 
write directory, for security. 
For example, an embedded scripting language cannot write outside of 
this path if it uses PhysFS for all of its I/O, which means that 
untrusted scripts can run more safely. Symbolic links can be disabled 
as well, for added safety. For file reading, the programmer lists 
directories and archives that form a "search path". 
Once the search path is defined, it becomes a single, 
transparent hierarchical filesystem. 
This makes for easy access to ZIP files in the same way as you access 
a file directly on the disk, and it makes it easy to ship a new archive 
that will override a previous archive on a per-file basis. 
Finally, PhysicsFS gives you platform-abstracted means to determine 
if CD-ROMs are available, the user's home directory, where in the 
real filesystem your program is running, etc.
Compiled for the Win32 target.

%package -n mingw32-physfs-static
Summary:       Static version of the MinGW Win32 compiled physfs library
Requires:      mingw32-physfs = %{version}-%{release}

%description -n mingw32-physfs-static
Static version of the MinGW Win32 compiled physfs library.

# Win64
%package -n mingw64-physfs
Summary:       MinGW compiled physfs library for the Win64 target

%description -n mingw64-physfs
MinGW compiled PhysicsFS, a library to provide abstract access 
to various archives. It is intended for use in video games, and the 
design was somewhat inspired by Quake 3's file subsystem. 
The programmer defines a "write directory" on the physical filesystem. 
No file writing done through the PhysicsFS API can leave that 
write directory, for security. 
For example, an embedded scripting language cannot write outside of 
this path if it uses PhysFS for all of its I/O, which means that 
untrusted scripts can run more safely. Symbolic links can be disabled 
as well, for added safety. For file reading, the programmer lists 
directories and archives that form a "search path". 
Once the search path is defined, it becomes a single, 
transparent hierarchical filesystem. 
This makes for easy access to ZIP files in the same way as you access 
a file directly on the disk, and it makes it easy to ship a new archive 
that will override a previous archive on a per-file basis. 
Finally, PhysicsFS gives you platform-abstracted means to determine 
if CD-ROMs are available, the user's home directory, where in the 
real filesystem your program is running, etc.
Compiled for the Win64 target.

%package -n mingw64-physfs-static
Summary:       Static version of the MinGW Win64 compiled physfs library
Requires:      mingw64-physfs = %{version}-%{release}

%description -n mingw64-physfs-static
Static version of the MinGW Win64 compiled physfs library.


%{?mingw_debug_package}

%prep
%setup -q -n physfs-%{version}

# Ensure we use system zlib
# don't use bundled lzma
rm -rf zlib123
rm -rf lzma


%build
%mingw_cmake . -DPHYSFS_BUILD_TEST=OFF -DPHYSFS_BUILD_WX_TEST=OFF -DPHYSFS_ARCHIVE_7Z=OFF

%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

mkdir -p %{buildroot}/%{_docdir}
cp CHANGELOG.txt CREDITS.txt LICENSE.txt TODO.txt %{buildroot}/%{_docdir}

find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-physfs
%{mingw32_bindir}/libphysfs.dll
%{mingw32_includedir}/physfs.h
%{mingw32_libdir}/libphysfs.dll.a
%doc %{_docdir}/*

%files -n mingw32-physfs-static
%{mingw32_libdir}/libphysfs.a

# Win64
%files -n mingw64-physfs
%{mingw64_bindir}/libphysfs.dll
%{mingw64_includedir}/physfs.h
%{mingw64_libdir}/libphysfs.dll.a
%doc %{_docdir}/*

%files -n mingw64-physfs-static
%{mingw64_libdir}/libphysfs.a


%changelog
* Mon Oct 14 2013 maci <maci@satgnu.net> - 2.0.3-4
- remove patch
- build without 7zip support, its unlikely mingw-lzma-sdk457 will ever
  work. Can be re-enabled when xz-devel support is implemented 
  http://icculus.org/pipermail/physfs/2010-December/000971.html


* Thu Jun 06 2013 Marcel Wysocki <maci@satgnu.net> - 2.0.3-3
- rebuilt for mingw-lzma-sdk457 package

* Tue May 14 2013 Marcel Wysocki <maci@satgnu.net> - 2.0.3-2
- spec cleanups

* Sat Apr 27 2013 Marcel Wysocki <maci@satgnu.net> - 2.0.3-1
- Initial release
