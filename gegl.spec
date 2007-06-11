#
Summary:	Generic image processing library
Name:		gegl
Version:	0.0.12
Release:	1
License:	GPL v2
Group:		Applications
Source0:	ftp://ftp.gtk.org/pub/gegl/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	dda7513cb4ab4b62528a9822e5c5751b
Patch0:		%{name}-build.patch
URL:		http://www.gegl.org/gegl/
BuildRequires:	OpenEXR-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	babl-devel
BuildRequires:	cairo-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	pango-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GEGL (Generic Graphics Library) is a graph based image processing
framework.

GEGLs original design was made to scratch GIMPs itches for a new
compositing and processing core. This core is being designed to have
minimal dependencies. and a simple well defined API.

%package devel
Summary:	Header files for gegl library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki gegl
Group:		Development/Libraries
# if base package contains shared library for which these headers are
#Requires:	%{name} = %{version}-%{release}
# if -libs package contains shared library for which these headers are
#Requires:	%{name}-libs = %{version}-%{release}

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
%{__aclocal}
%{__autoconf}
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
%dir %{_libdir}/gegl-*
%{_libdir}/gegl-*/*.so
%attr(755,root,root) %{_libdir}/libgegl-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/gegl-*
%{_libdir}/libgegl-*.la
%{_libdir}/libgegl-*.so
%{_pkgconfigdir}/gegl.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgegl-1.0.a
