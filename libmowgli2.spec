#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	Development framework for C (like GLib)
Summary(pl.UTF-8):	Szkielet programistyczny dla C (podobny do GLiba)
Name:		libmowgli2
Version:	2.0.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://github.com/atheme/libmowgli-2/archive/libmowgli-%{version}.tar.gz
# Source0-md5:	0b8cf8b66d745d40f186e3cbd22fdc0e
URL:		https://github.com/atheme/libmowgli-2/
BuildRequires:	openssl-devel
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mowgli is a development framework for C (like GLib), which provides
high performance and highly flexible algorithms. It can be used as a
suppliment to GLib (to add additional functions (dictionaries,
hashes), or replace some of the slow GLib functions (like list
manipulation), or stand alone. It also provides a powerful hook system
and convenient logging for your code, as well as a high performance
block allocator.

%description -l pl.UTF-8
mowgli to szkielet programistyczny dla C (podobny do GLiba)
udostępniający wysoko wydajne i elastyczne algorytmy. Może być używany
jako suplement do GLiba (dodający nowe funkcje, takie jak słowniki czy
hasze) albo do zastąpienia niektórych wolnych funkcji GLiba (jak
operacje na listach), albo samodzielnie. Udostępnia także potężny
system uchwytów i wygodnego logowania, a także wysoko wydajny alokator
bloków.

%package devel
Summary:	Header files for libmowgli
Summary(pl.UTF-8):	Pliki nagłówkowe libmowgli
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libmowgli.

%description devel -l pl.UTF-8
Pliki nagłówkowe libmowgli.

%package static
Summary:	Static libmowgli library
Summary(pl.UTF-8):	Biblioteka statyczna libmowgli
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmowgli library.

%description static -l pl.UTF-8
Biblioteka statyczna libmowgli.

%prep
%setup -q -n libmowgli-2-libmowgli-%{version}

%{__sed} -i -e '/^\.SILENT/d' buildsys.mk.in

%build
%configure \
	%{?with_static_libs:--enable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
%attr(755,root,root) %{_libdir}/libmowgli-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmowgli-2.so.0

%files devel
%defattr(644,root,root,755)
%doc doc/{BOOST,design-concepts.txt}
%attr(755,root,root) %{_libdir}/libmowgli-2.so
%{_includedir}/libmowgli-2
%{_pkgconfigdir}/libmowgli-2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmowgli-2.a
%endif
