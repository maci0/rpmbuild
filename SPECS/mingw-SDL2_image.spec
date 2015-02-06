%?mingw_package_header

Name:           mingw-SDL2_image
Version:        2.0.0
Release:        4%{?dist}
Summary:        MinGW Windows port of the Image loading library for SDL2

License:        LGPLv2+
Group:          Development/Libraries
URL:            http://www.libSDL.org/projects/SDL_image/
Source0:        http://www.libSDL.org/projects/SDL_image/release/SDL2_image-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libwebp


BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libwebp


%description
Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL2 surfaces.


# Win32
%package -n mingw32-SDL2_image
Summary:        MinGW Windows port of the Image loading library for SDL2

%description -n mingw32-SDL2_image
Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL2 surfaces.

# Win64
%package -n mingw64-SDL2_image
Summary:        MinGW Windows port of the Image loading library for SDL2

%description -n mingw64-SDL2_image
Simple DirectMedia Layer (SDL2) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL2 surfaces.


%?mingw_debug_package


%prep
%setup -q -n SDL2_image-%{version}


%build
# the --disabled-*-shared lines below stops SDL2_image from loading those
# libraries at link time. Instead they are loaded when needed.
%mingw_configure \
    --disable-jpg-shared \
    --disable-png-shared \
    --disable-tif-shared \
    --disable-webp-shared \
    --disable-static
#    --disable-dependency-tracking \

%mingw_make %{?smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install


# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Strip wrong end of line encoding
sed -i 's/\r$//' README.txt CHANGES.txt COPYING.txt

# Win32
%files -n mingw32-SDL2_image
%doc README.txt CHANGES.txt COPYING.txt
%{mingw32_bindir}/SDL2_image.dll
%{mingw32_libdir}/libSDL2_image.dll.a
%{mingw32_libdir}/pkgconfig/SDL2_image.pc
%{mingw32_includedir}/SDL2

# Win64
%files -n mingw64-SDL2_image
%doc README.txt CHANGES.txt COPYING.txt
%{mingw64_bindir}/SDL2_image.dll
%{mingw64_libdir}/libSDL2_image.dll.a
%{mingw64_libdir}/pkgconfig/SDL2_image.pc
%{mingw64_includedir}/SDL2


%changelog
* Fri Feb 06 2015 maci <maci@satgnu.net> - 2.0.0-4
- Strip wrong end of line encoding in README.txt CHANGES.txt COPYING.txt
- Fedora 21 rebuild

* Mon Jul 21 2014 maci <maci@satgnu.net> - 2.0.0-3
- Fix homepage URL

* Tue May 13 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.0-2
- Removed redundant BuildRequires

* Mon May 12 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.0-1
- Initial rpm
