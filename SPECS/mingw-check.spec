%{?mingw_package_header}

Name:           mingw-example
Version:        1.0.0
Release:        1%{?dist}
Summary:        MinGW compiled example library

License:        LGPLv2+
URL:            http://fedoraproject.org
Source0:        http://fedoraproject.org/example-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib


%description
MinGW compiled example library.


# If a package maintainer wishes to bundle static libraries then they
# can be placed in -static subpackages. Otherwise, the -static subpackages
# can be dropped

# Win32
%package -n mingw32-example
Summary:       MinGW compiled example library for the Win32 target

%description -n mingw32-example
MinGW compiled example library for the Win32 target.

%package -n mingw32-example-static
Summary:       Static version of the MinGW Win32 compiled example library
Requires:      mingw32-example = %{version}-%{release}

%description -n mingw32-example-static
Static version of the MinGW Win32 compiled example library.

# Win64
%package -n mingw64-example
Summary:       MinGW compiled example library for the Win64 target

%description -n mingw64-example
MinGW compiled example library for the Win64 target.

%package -n mingw64-example-static
Summary:       Static version of the MinGW Win64 compiled example library
Requires:      mingw64-example = %{version}-%{release}

%description -n mingw64-example-static
Static version of the MinGW Win64 compiled example library.


%{?mingw_debug_package}


%prep
%setup -q -n example-%{version}


%build
%mingw_configure --enable-static --enable-shared --enable-foo
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

%mingw_find_lang example


# Note: there should be no %%files section for the main package!

# Static subpackages are optional (as mentioned earlier)

# Win32
%files -n mingw32-example -f mingw32-example.lang
%{mingw32_bindir}/libexample-0.dll
%{mingw32_includedir}/example/
%{mingw32_libdir}/libexample.dll.a
%{mingw32_libdir}/pkgconfig/example.pc

%files -n mingw32-example-static
%{mingw32_libdir}/libexample.a

# Win64
%files -n mingw64-example -f mingw64-example.lang
%{mingw64_bindir}/libexample-0.dll
%{mingw64_includedir}/example/
%{mingw64_libdir}/libexample.dll.a
%{mingw64_libdir}/pkgconfig/example.pc

%files -n mingw64-example-static
%{mingw64_libdir}/libexample-0.a


%changelog
* Tue Feb 10 2015 Marcel Wysocki <maci@satgnu.net> - 1.0.0-1
- Initial release
