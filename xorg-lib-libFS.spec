# $Rev: 3245 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	FS library
Summary(pl):	Biblioteka FS
Name:		xorg-lib-libFS
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libFS-%{version}.tar.bz2
# Source0-md5:	26e469cf986ad7d09f0babac7ad30424
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-lib-xtrans-devel
BuildRoot:	%{tmpdir}/libFS-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
FS library.

%description -l pl
Biblioteka FS.


%package devel
Summary:	Header files libFS development
Summary(pl):	Pliki nag³ówkowe do biblioteki libFS
Group:		X11/Development/Libraries
Requires:	xorg-lib-libFS = %{version}-%{release}
Requires:	xorg-proto-fontsproto-devel

%description devel
FS library.

This package contains the header files needed to develop programs that
use these libFS.

%description devel -l pl
Biblioteka FS.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libFS.


%package static
Summary:	Static libFS libraries
Summary(pl):	Biblioteki statyczne libFS
Group:		Development/Libraries
Requires:	xorg-lib-libFS-devel = %{version}-%{release}

%description static
FS library.

This package contains the static libFS library.

%description static -l pl
Biblioteka FS.

Pakiet zawiera statyczn± bibliotekê libFS.


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
%doc ChangeLog
%attr(755,root,wheel) %{_libdir}/libFS.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/fonts/*.h
%{_libdir}/libFS.la
%attr(755,root,wheel) %{_libdir}/libFS.so
%{_pkgconfigdir}/libfs.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libFS.a
