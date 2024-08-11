Summary:	libFS - X Font Service client library
Summary(pl.UTF-8):	libFS - biblioteka kliencka usługi fontów X (X Font Service)
Name:		xorg-lib-libFS
Version:	1.0.10
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libFS-%{version}.tar.xz
# Source0-md5:	c5cc0942ed39c49b8fcd47a427bd4305
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.70
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains libFS, an X Font Service client library. It's
used by clients of X Font Servers (xfs), such as xfsinfo, xfslsfonts,
and the X servers themselves.

%description -l pl.UTF-8
Ten pakiet zawiera libFS - bibliotekę kliencką usługi fontów X (X Font
Service). Jest ona używana przez klientów serwerów fontów X (xfs - X
Font Servers), takich jak xfsinfo, xfslsfonts czy same serwery X.

%package devel
Summary:	Header files for libFS library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libFS
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-fontsproto-devel
Requires:	xorg-proto-xproto-devel >= 7.0.17

%description devel
libFS - biblioteka kliencka usługi fontów X (X Font Service).

This package contains the header files needed to develop programs that
use libFS.

%description devel -l pl.UTF-8
libFS - biblioteka kliencka usługi fontów X (X Font Service).

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libFS.

%package static
Summary:	Static libFS library
Summary(pl.UTF-8):	Biblioteka statyczna libFS
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libFS - biblioteka kliencka usługi fontów X (X Font Service).

This package contains the static libFS library.

%description static -l pl.UTF-8
libFS - biblioteka kliencka usługi fontów X (X Font Service).

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
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/libFS/FSlib.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libFS.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libFS.so.6

%files devel
%defattr(644,root,root,755)
%doc doc/FSlib.txt
%attr(755,root,root) %{_libdir}/libFS.so
%{_libdir}/libFS.la
%{_includedir}/X11/fonts/FSlib.h
%{_pkgconfigdir}/libfs.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libFS.a
