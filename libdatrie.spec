#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libdatrie
Version  : 0.2.12
Release  : 8
URL      : ftp://linux.thai.net/pub/thailinux/software/libthai/libdatrie-0.2.12.tar.xz
Source0  : ftp://linux.thai.net/pub/thailinux/software/libthai/libdatrie-0.2.12.tar.xz
Summary  : Double-array trie library
Group    : Development/Tools
License  : LGPL-2.1
Requires: libdatrie-bin
Requires: libdatrie-lib
Requires: libdatrie-license
Requires: libdatrie-man
BuildRequires : doxygen
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
datrie - Double-Array Trie Library
==================================
This is an implementation of double-array structure for representing trie,
as proposed by Junichi Aoe [1].

%package bin
Summary: bin components for the libdatrie package.
Group: Binaries
Requires: libdatrie-license
Requires: libdatrie-man

%description bin
bin components for the libdatrie package.


%package dev
Summary: dev components for the libdatrie package.
Group: Development
Requires: libdatrie-lib
Requires: libdatrie-bin
Provides: libdatrie-devel

%description dev
dev components for the libdatrie package.


%package dev32
Summary: dev32 components for the libdatrie package.
Group: Default
Requires: libdatrie-lib32
Requires: libdatrie-bin
Requires: libdatrie-dev

%description dev32
dev32 components for the libdatrie package.


%package doc
Summary: doc components for the libdatrie package.
Group: Documentation
Requires: libdatrie-man

%description doc
doc components for the libdatrie package.


%package lib
Summary: lib components for the libdatrie package.
Group: Libraries
Requires: libdatrie-license

%description lib
lib components for the libdatrie package.


%package lib32
Summary: lib32 components for the libdatrie package.
Group: Default
Requires: libdatrie-license

%description lib32
lib32 components for the libdatrie package.


%package license
Summary: license components for the libdatrie package.
Group: Default

%description license
license components for the libdatrie package.


%package man
Summary: man components for the libdatrie package.
Group: Default

%description man
man components for the libdatrie package.


%prep
%setup -q -n libdatrie-0.2.12
pushd ..
cp -a libdatrie-0.2.12 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530989422
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1530989422
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libdatrie
cp COPYING %{buildroot}/usr/share/doc/libdatrie/COPYING
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/trietool
/usr/bin/trietool-0.2

%files dev
%defattr(-,root,root,-)
/usr/include/datrie/alpha-map.h
/usr/include/datrie/trie.h
/usr/include/datrie/triedefs.h
/usr/include/datrie/typedefs.h
/usr/lib64/libdatrie.so
/usr/lib64/pkgconfig/datrie-0.2.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libdatrie.so
/usr/lib32/pkgconfig/32datrie-0.2.pc
/usr/lib32/pkgconfig/datrie-0.2.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libdatrie/*
/usr/share/doc/datrie/html/alpha-map_8h.html
/usr/share/doc/datrie/html/annotated.html
/usr/share/doc/datrie/html/bc_s.png
/usr/share/doc/datrie/html/bdwn.png
/usr/share/doc/datrie/html/classes.html
/usr/share/doc/datrie/html/closed.png
/usr/share/doc/datrie/html/dir_23cbef3b1b2df757deb7708cc4a2d793.html
/usr/share/doc/datrie/html/doc.png
/usr/share/doc/datrie/html/doxygen.css
/usr/share/doc/datrie/html/doxygen.png
/usr/share/doc/datrie/html/dynsections.js
/usr/share/doc/datrie/html/files.html
/usr/share/doc/datrie/html/folderclosed.png
/usr/share/doc/datrie/html/folderopen.png
/usr/share/doc/datrie/html/functions.html
/usr/share/doc/datrie/html/functions_vars.html
/usr/share/doc/datrie/html/globals.html
/usr/share/doc/datrie/html/globals_defs.html
/usr/share/doc/datrie/html/globals_func.html
/usr/share/doc/datrie/html/globals_type.html
/usr/share/doc/datrie/html/index.html
/usr/share/doc/datrie/html/jquery.js
/usr/share/doc/datrie/html/menu.js
/usr/share/doc/datrie/html/menudata.js
/usr/share/doc/datrie/html/nav_f.png
/usr/share/doc/datrie/html/nav_g.png
/usr/share/doc/datrie/html/nav_h.png
/usr/share/doc/datrie/html/open.png
/usr/share/doc/datrie/html/splitbar.png
/usr/share/doc/datrie/html/struct__Trie.html
/usr/share/doc/datrie/html/struct__TrieIterator.html
/usr/share/doc/datrie/html/struct__TrieState.html
/usr/share/doc/datrie/html/sync_off.png
/usr/share/doc/datrie/html/sync_on.png
/usr/share/doc/datrie/html/tab_a.png
/usr/share/doc/datrie/html/tab_b.png
/usr/share/doc/datrie/html/tab_h.png
/usr/share/doc/datrie/html/tab_s.png
/usr/share/doc/datrie/html/tabs.css
/usr/share/doc/datrie/html/trie_8h.html
/usr/share/doc/datrie/html/triedefs_8h.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdatrie.so.1
/usr/lib64/libdatrie.so.1.3.5

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libdatrie.so.1
/usr/lib32/libdatrie.so.1.3.5

%files license
%defattr(-,root,root,-)
/usr/share/doc/libdatrie/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/trietool-0.2.1
/usr/share/man/man1/trietool.1
