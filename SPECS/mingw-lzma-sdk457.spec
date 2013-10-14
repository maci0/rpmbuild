%{?mingw_package_header}

Name:		mingw-lzma-sdk457
Version:	4.57
Release:	3%{?dist}
Summary:	SDK for lzma compression
Group:		Applications/Archiving
License:	LGPLv2+
URL:		http://sourceforge.net/projects/sevenzip/
Source0:	http://downloads.sourceforge.net/sevenzip/lzma457.tar.bz2
Patch0:		lzma-sdk-4.5.7-sharedlib.patch

BuildArch:      noarch

BuildRequires:  mingw32-gcc-c++

BuildRequires:  mingw64-gcc-c++



%description
MinGW compiled version of LZMA SDK. 
It provides the documentation, samples, header files, libraries,
and tools you need to develop applications that use LZMA compression.

LZMA is default and general compression method of 7z format
in 7-Zip compression program (7-zip.org). LZMA provides high
compression ratio and very fast decompression.

LZMA is an improved version of famous LZ77 compression algorithm. 
It was improved in way of maximum increasing of compression ratio,
keeping high decompression speed and low memory requirements for
decompressing.

# Win32
%package -n mingw32-lzma-sdk457
Summary:      SDK for lzma compression, compiled for the Win32 target

%description -n mingw32-lzma-sdk457
LZMA SDK provides the documentation, samples, header files, libraries,
and tools you need to develop applications that use LZMA compression.

LZMA is default and general compression method of 7z format
in 7-Zip compression program (7-zip.org). LZMA provides high
compression ratio and very fast decompression.

LZMA is an improved version of famous LZ77 compression algorithm. 
It was improved in way of maximum increasing of compression ratio,
keeping high decompression speed and low memory requirements for
decompressing.

Compiled for the Win32 target.


# Win64
%package -n mingw64-lzma-sdk457
Summary:      SDK for lzma compression, compiled for the Win64 target

%description -n mingw64-lzma-sdk457
LZMA SDK provides the documentation, samples, header files, libraries,
and tools you need to develop applications that use LZMA compression.

LZMA is default and general compression method of 7z format
in 7-Zip compression program (7-zip.org). LZMA provides high
compression ratio and very fast decompression.

LZMA is an improved version of famous LZ77 compression algorithm. 
It was improved in way of maximum increasing of compression ratio,
keeping high decompression speed and low memory requirements for
decompressing.

Compiled for the Win64 target.

%{?mingw_debug_package}


%prep
%setup -q -c -n lzma457
%patch0 -p1 -b .shared

rm lzma.exe

for f in .h .c .cpp .dsw .dsp .java .cs .txt makefile; do
	find . -iname "*$f" | xargs chmod -x
done

%build

sed -i 's/liblzmasdk457.so/liblzmasdk457.dll/' CPP/7zip/Compress/LZMA_Alone/makefile.gcc
sed -i 's/-Wl,-soname=$(LIBRARYMINOR)//' CPP/7zip/Compress/LZMA_Alone/makefile.gcc
sed -i 's/$(CXX) -o $(LIBRARYMAJOR)/$(CXX) -o $(LIBRARY)/' CPP/7zip/Compress/LZMA_Alone/makefile.gcc

mkdir build_win32/
mkdir build_win64/

cp -a `ls -A | grep -vE "build_win"` build_win32
cp -a `ls -A | grep -vE "build_win"` build_win64

pushd build_win32/CPP/7zip/Compress/LZMA_Alone
%{mingw32_make} %{?_smp_mflags} -f makefile.gcc clean all \
CXX="%mingw32_cc %mingw32_cflags -DUNICODE -D_UNICODE" \
CXX_C="%mingw32_cc %mingw32_cflags -DUNICODE -D_UNICODE" \
LIB="-lole32 -luuid -luser32 -lm -lstdc++" \
IS_MINGW="1"
popd

pushd build_win64/CPP/7zip/Compress/LZMA_Alone
%{mingw64_make} %{?_smp_mflags} -f makefile.gcc clean all \
CXX="%mingw64_cc %mingw64_cflags -DUNICODE -D_UNICODE" \
CXX_C="%mingw64_cc %mingw64_cflags -DUNICODE -D_UNICODE" \
LIB="-lole32 -luuid -luser32 -lm -lstdc++" \
IS_MINGW="1"
popd

%install
mkdir -p %{buildroot}%{mingw32_bindir}
mkdir -p %{buildroot}%{mingw64_bindir}

mkdir -p %{buildroot}%{mingw32_libdir}
mkdir -p %{buildroot}%{mingw64_libdir}

install -m0755 build_win32/CPP/7zip/Compress/LZMA_Alone/liblzmasdk457.dll %{buildroot}%{mingw32_bindir}
install -m0755 build_win64/CPP/7zip/Compress/LZMA_Alone/liblzmasdk457.dll %{buildroot}%{mingw64_bindir}

mkdir -p %{buildroot}/%{mingw32_includedir}/lzma457/
find -iname '*.h' | grep -v build_win | xargs -I {} install -m0644 -D {} %{buildroot}/%{mingw32_includedir}/lzma457/{}

mkdir -p %{buildroot}/%{mingw64_includedir}/lzma457/
find -iname '*.h' | grep -v build_win | xargs -I {} install -m0644 -D {} %{buildroot}/%{mingw64_includedir}/lzma457/{}

# Win32
%files -n mingw32-lzma-sdk457
%{mingw32_bindir}/liblzmasdk457.dll
%{mingw32_includedir}/lzma457/
%{mingw32_libdir}/liblzmasdk457.dll.a

# Win64
%files -n mingw64-lzma-sdk457
%{mingw64_bindir}/liblzmasdk457.dll
%{mingw64_includedir}/lzma457/
%{mingw64_libdir}/liblzmasdk457.dll.a


%changelog
* Mon Oct 14 2013 maci <maci@satgnu.net> - 4.57-3
- remove lgpl file
- remove post* triggers
- dont change file encoding
- remove unneeded deps
- remove -fPIC as it was ignored anyway

* Thu Jun 06 2013 Marcel Wysocki <maci@satgnu.net> - 4.57-2
- add rsync build dep
- add missing g++ build dep

* Wed Jun 05 2013 Marcel Wysocki <maci@satgnu.net> - 4.57-1
- initial mingw port of fedora package lzma-sdk457-4.57-4

