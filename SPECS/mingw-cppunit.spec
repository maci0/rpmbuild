%{?mingw_package_header}

Name:           mingw-cppunit
Version:        1.12.1
Release:        15%{?dist}
Summary:        MinGW Windows C++ unit testing framework

Group:          Development/Libraries
License:        LGPLv2+
URL:            http://cppunit.sourceforge.net/
Source0:        http://downloads.sourceforge.net/cppunit/cppunit-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils

Requires: pkgconfig

%description
CppUnit is the C++ port of the famous JUnit framework for unit testing.
Test output is in XML for automatic testing and GUI based for supervised 
tests.

MinGW Windows C++ unit testing framework.


%package -n mingw32-cppunit
Summary:        MinGW Windows C++ unit testing framework

%description -n mingw32-cppunit
CppUnit is the C++ port of the famous JUnit framework for unit testing.
Test output is in XML for automatic testing and GUI based for supervised
tests.

%package -n mingw64-cppunit
Summary:        MinGW Windows C++ unit testing framework

%description -n mingw64-cppunit
CppUnit is the C++ port of the famous JUnit framework for unit testing.
Test output is in XML for automatic testing and GUI based for supervised
tests.

MinGW Windows C++ unit testing framework.

%{?mingw_debug_package}

%prep
%setup -q -n cppunit-%{version}
for file in THANKS ChangeLog NEWS; do
   iconv -f latin1 -t utf8 < $file > ${file}.utf8
   touch -c -r $file ${file}.utf8
   mv ${file}.utf8 $file
done


%build
%mingw_configure --disable-static --disable-doxygen
%mingw_make %{?_smp_mflags}


%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
# Remove the .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n mingw32-cppunit
%doc AUTHORS COPYING NEWS README THANKS ChangeLog TODO BUGS doc/FAQ
%{mingw32_bindir}/cppunit-config
%{mingw32_bindir}/DllPlugInTester.exe
%{mingw32_includedir}/cppunit/
%{mingw32_bindir}/libcppunit-*.dll
%{mingw32_libdir}/pkgconfig/cppunit.pc
%{mingw32_libdir}/libcppunit.dll.a
%{mingw32_datadir}/aclocal/cppunit.m4
%exclude %{mingw32_mandir}/man1/cppunit-config.1

%files -n mingw64-cppunit
%doc AUTHORS COPYING NEWS README THANKS ChangeLog TODO BUGS doc/FAQ
%{mingw64_bindir}/cppunit-config
%{mingw64_bindir}/DllPlugInTester.exe
%{mingw64_includedir}/cppunit/
%{mingw64_bindir}/libcppunit-*.dll
%{mingw64_libdir}/pkgconfig/cppunit.pc
%{mingw64_libdir}/libcppunit.dll.a
%{mingw64_datadir}/aclocal/cppunit.m4
%exclude %{mingw64_mandir}/man1/cppunit-config.1


%changelog
* Mon Aug 03 2015 Marcel Wysocki <maci@satgnu.net> - 1.12.1-15
- Add support for mingw64

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Kalev Lember <kalevlember@gmail.com> - 1.12.1-9
- Remove the .la files

* Wed Mar 07 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12.1-8
- Renamed the source package to mingw-cppunit (RHBZ #800853)
- Use mingw macros without leading underscore
- Dropped unneeded RPM tags

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.12.1-7
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 22 2011 Kalev Lember <kalev@smartlink.ee> - 1.12.1-5
- Rebuilt for pseudo-reloc version mismatch (#698827)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct  4 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.12.1-3
- Rebuild for MinGW debuginfo breakage

* Mon Aug 17 2009 Nicolas Chauvet <kwizart@gmail.com> - 1.12.1-2
- Fix BR mingw32-gcc-c++
- Update description
- Disable duplicated docs with native package.

* Mon Jan  5 2009 Nicolas Chauvet <kwizart@gmail.com> - 1.12.1-1
- Initial package based on original cppunit.spec

