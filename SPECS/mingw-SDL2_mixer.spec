%{?mingw_package_header}

Name:           mingw-SDL2_mixer
Version:        2.0.0
Release:        3%{?dist}
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library

License:        zlib
Group:          Development/Libraries
URL:            http://www.libSDL.org/projects/SDL_mixer/
Source0:        http://www.libSDL.org/projects/SDL_mixer/release/SDL2_mixer-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-SDL2
BuildRequires:  mingw32-libvorbis
BuildRequires:  mingw32-flac

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-SDL2
BuildRequires:  mingw64-libvorbis
BuildRequires:  mingw64-flac

%description
A simple multi-channel audio mixer for SDL2. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.


# Win32
%package -n mingw32-SDL2_mixer
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library

%description -n mingw32-SDL2_mixer
A simple multi-channel audio mixer for SDL2. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.

# Win64
%package -n mingw64-SDL2_mixer
Summary:        MinGW Windows port of Simple DirectMedia Layer's Sample Mixer Library

%description -n mingw64-SDL2_mixer
A simple multi-channel audio mixer for SDL2. It supports 4 channels of
16 bit stereo audio, plus a single channel of music, mixed by the popular
MikMod MOD library.


# Automatically create a debuginfo package
%?mingw_debug_package


%prep
%setup -q -n SDL2_mixer-%{version}


%build
%mingw_configure \
    --disable-static

%mingw_make %{?_smp_mflags}


%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete


# Win32
%files -n mingw32-SDL2_mixer
%doc README.txt CHANGES.txt COPYING.txt
%{mingw32_bindir}/SDL2_mixer.dll
%{mingw32_libdir}/libSDL2_mixer.dll.a
%{mingw32_libdir}/pkgconfig/SDL2_mixer.pc
%{mingw32_includedir}/SDL2

# Win64
%files -n mingw64-SDL2_mixer
%doc README.txt CHANGES.txt COPYING.txt
%{mingw64_bindir}/SDL2_mixer.dll
%{mingw64_libdir}/libSDL2_mixer.dll.a
%{mingw64_libdir}/pkgconfig/SDL2_mixer.pc
%{mingw64_includedir}/SDL2


%changelog
* Mon Jul 21 2014 maci <maci@satgnu.net> - 2.0.0-3
- Fix homepage URL

* Tue May 13 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.0-2
- Removed redundant BuildRequires

* Mon May 12 2014 Marcel Wysocki <maci@satgnu.net> - 2.0.0-1
- Initial rpm
