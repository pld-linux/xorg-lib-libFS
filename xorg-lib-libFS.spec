Summary:	FS library
Summary(pl):	Biblioteka FS
Name:		xorg-lib-libFS
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/lib/libFS-%{version}.tar.bz2
# Source0-md5:	13f66d54031b257833714e5d1d71ced9
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-xtrans-devel
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FS library.

%description -l pl
Biblioteka FS.

%package devel
Summary:	Header files libFS development
Summary(pl):	Pliki nag��wkowe do biblioteki libFS
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-proto-fontsproto-devel

%description devel
FS library.

This package contains the header files needed to develop programs that
use these libFS.

%description devel -l pl
Biblioteka FS.

Pakiet zawiera pliki nag��wkowe niezb�dne do kompilowania program�w
u�ywaj�cych biblioteki libFS.

%package static
Summary:	Static libFS library
Summary(pl):	Biblioteka statyczna libFS
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
FS library.

This package contains the static libFS library.

%description static -l pl
Biblioteka FS.

Pakiet zawiera statyczn� bibliotek� libFS.

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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libFS.so
%{_libdir}/libFS.la
%{_includedir}/X11/fonts/*.h
%{_pkgconfigdir}/libfs.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libFS.a
