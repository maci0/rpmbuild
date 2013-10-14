%{?mingw_package_header}

Name:           mingw-enet
Version:        1.3.3
Release:        1%{?dist}
Summary:        Thin, simple and robust network layer on top of UDP, MinGW compiled

License:        MIT
Group:          System Environment/Libraries
URL:            http://enet.bespin.org/
Source0:        http://enet.bespin.org/download/enet-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils


%description
MinGW compiled version of ENet, a relatively thin, simple and robust network communication layer on
top of UDP (User Datagram Protocol). The primary feature it provides is
optional reliable, in-order delivery of packets.

ENet is NOT intended to be a general purpose high level networking library
that handles authentication, lobbying, server discovery, compression,
encryption and other high level, often application level or dependent tasks.


# Win32
%package -n mingw32-enet
Summary:       Thin, simple and robust network layer on top of UDP, compiled for the Win32 target

%description -n mingw32-enet
ENet is a relatively thin, simple and robust network communication layer on
top of UDP (User Datagram Protocol). The primary feature it provides is
optional reliable, in-order delivery of packets.

ENet is NOT intended to be a general purpose high level networking library
that handles authentication, lobbying, server discovery, compression,
encryption and other high level, often application level or dependent tasks.

Compiled for the Win32 target.


%package -n mingw32-enet-static
Summary:       Static version of the MinGW Win32 compiled enet library
Requires:      mingw32-enet = %{version}-%{release}

%description -n mingw32-enet-static
Static version of the MinGW Win32 compiled enet library.

# Win64
%package -n mingw64-enet
Summary:      Thin, simple and robust network layer on top of UDP, compiled for the Win64 target

%description -n mingw64-enet
ENet is a relatively thin, simple and robust network communication layer on
top of UDP (User Datagram Protocol). The primary feature it provides is
optional reliable, in-order delivery of packets.

ENet is NOT intended to be a general purpose high level networking library
that handles authentication, lobbying, server discovery, compression,
encryption and other high level, often application level or dependent tasks.

Compiled for the Win64 target.

%package -n mingw64-enet-static
Summary:       Static version of the MinGW Win64 compiled enet library
Requires:      mingw64-enet = %{version}-%{release}

%description -n mingw64-enet-static
Static version of the MinGW Win64 compiled enet library.


%{?mingw_debug_package}


%prep
%setup -q -n enet-%{version}


%build
%mingw_configure --enable-static --enable-shared
cp -a include/enet build_win32/
cp -a include/enet build_win64/
%mingw_make %{?_smp_mflags}


# generate shared library by hand (not implemented in Makefile)
# same hack exists in the fedora enet package
pushd build_win32/
%mingw32_cc -shared %mingw32_cflags *.o -lws2_32 -lwinmm  \
  -o libenet-0.dll
popd
pushd build_win64/
%mingw64_cc -shared %mingw64_cflags *.o -lws2_32 -lwinmm  \
  -o libenet-0.dll
popd


%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# 
mkdir $RPM_BUILD_ROOT/%{mingw32_bindir}/
mkdir $RPM_BUILD_ROOT/%{mingw64_bindir}/
cp build_win32/libenet-0.dll $RPM_BUILD_ROOT/%{mingw32_bindir}/
cp build_win64/libenet-0.dll $RPM_BUILD_ROOT/%{mingw64_bindir}/


# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

# Note: there should be no %%files section for the main package!

# Static subpackages are optional (as mentioned earlier)

# Win32
%files -n mingw32-enet
%{mingw32_bindir}/libenet-0.dll
%{mingw32_includedir}/enet/
#%{mingw32_libdir}/libenet.dll.a
%{mingw32_libdir}/pkgconfig/libenet.pc

%files -n mingw32-enet-static
%{mingw32_libdir}/libenet.a

# Win64
%files -n mingw64-enet
%{mingw64_bindir}/libenet-0.dll
%{mingw64_includedir}/enet/
#%{mingw64_libdir}/libenet.dll.a
%{mingw64_libdir}/pkgconfig/libenet.pc

%files -n mingw64-enet-static
%{mingw64_libdir}/libenet.a

%changelog
* Sat Apr 20 2013 Marcel Wysocki <maci@satgnu.net> - 1.3.3-2
- initial build, works but is hacky
