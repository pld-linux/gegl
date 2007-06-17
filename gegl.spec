Summary:	Generic image processing library
Summary(pl.UTF-8):	Ogólna biblioteka przetwarzania obrazu
Name:		gegl
Version:	0.0.12
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	ftp://ftp.gtk.org/pub/gegl/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	dda7513cb4ab4b62528a9822e5c5751b
Patch0:		%{name}-build.patch
URL:		http://www.gegl.org/
BuildRequires:	OpenEXR-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	babl-devel >= 0.0.14
BuildRequires:	cairo-devel
BuildRequires:	enscript
BuildRequires:	glib2-devel >= 1:2.6.4
BuildRequires:	gtk+2-devel >= 2:2.8.6
BuildRequires:	graphviz
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.14.0
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.10.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GEGL (Generic Graphics Library) is a graph based image processing
framework.

GEGL's original design was made to scratch GIMP's itches for a new
compositing and processing core. This core is being designed to have
minimal dependencies and a simple well defined API.

%description -l pl.UTF-8
GEGL (Generic Graphics Library) to oparty na grafice szkielet do
przetwarzania obrazu.

Pierwotny projekt biblioteki GEGL powstał z myślą o nowym rdzeniu do
składania i przetwarzania obrazu w GIMP-ie. Rdzeń ten jest
projektowany tak, by miał minimalne zależności i proste, dobrze
zdefiniowane API.

%package devel
Summary:	Header files for gegl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gegl
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	babl-devel >= 0.0.14
Requires:	glib2-devel >= 1:2.6.4

%description devel
Header files for gegl library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki gegl.

%package static
Summary:	Static gegl library
Summary(pl.UTF-8):	Statyczna biblioteka gegl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gegl library.

%description static -l pl.UTF-8
Statyczna biblioteka gegl.

%prep
%setup -q
%patch0 -p1

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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gegl
%attr(755,root,root) %{_libdir}/libgegl-*.so.*.*.*
%dir %{_libdir}/gegl-*
%attr(755,root,root) %{_libdir}/gegl-*/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgegl-*.so
%{_libdir}/libgegl-*.la
%{_includedir}/gegl-*
%{_pkgconfigdir}/gegl.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgegl-1.0.a
