Summary:	FS library
Summary(pl.UTF-8):	Biblioteka FS
Name:		xorg-lib-libFS
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libFS-%{version}.tar.bz2
# Source0-md5:	ecf2d6a27da053500283e803efa2a808
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-util-util-macros >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FS library.

%description -l pl.UTF-8
Biblioteka FS.

%package devel
Summary:	Header files for libFS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libFS
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-fontsproto-devel

%description devel
FS library.

This package contains the header files needed to develop programs that
use libFS.

%description devel -l pl.UTF-8
Biblioteka FS.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libFS.

%package static
Summary:	Static libFS library
Summary(pl.UTF-8):	Biblioteka statyczna libFS
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
FS library.

This package contains the static libFS library.

%description static -l pl.UTF-8
Biblioteka FS.

Pakiet zawiera statyczną bibliotekę libFS.

%prep
%setup -q -n libFS-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libFS.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libFS.so.6

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libFS.so
%{_libdir}/libFS.la
%{_includedir}/X11/fonts/*.h
%{_pkgconfigdir}/libfs.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libFS.a
