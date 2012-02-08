#
# Conditional build:
%bcond_with	mmx	# use MMX instructions
%bcond_with	sse	# use SSE instructions
%bcond_without	doc	# apidocs
%bcond_without	vala	# Vala API
#
%ifarch %{x8664} athlon pentium3 pentium4
%define	with_mmx	1
%endif
%ifarch %{x8664} pentium3 pentium4
%define	with_sse	1
%endif
Summary:	Generic image processing library
Summary(pl.UTF-8):	Ogólna biblioteka przetwarzania obrazu
Name:		gegl
Version:	0.1.8
Release:	3
License:	LGPL v3+
Group:		Libraries
Source0:	ftp://ftp.gimp.org/pub/gegl/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	c8279b86b3d584ee4f503839fc500425
Patch0:		%{name}-lua.patch
Patch1:		%{name}-ffmpeg.patch
Patch2:		%{name}-ruby1.9.patch
URL:		http://www.gegl.org/
BuildRequires:	OpenEXR-devel
BuildRequires:	SDL-devel
BuildRequires:	UMFPACK-devel
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.11
BuildRequires:	babl-devel >= 0.1.6
BuildRequires:	cairo-devel
BuildRequires:	enscript
BuildRequires:	exiv2-devel
BuildRequires:	ffmpeg-devel >= 0.8
BuildRequires:	gdk-pixbuf2-devel >= 2.18.0
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	graphviz
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	jasper-devel >= 1.900.1
BuildRequires:	lensfun-devel >= 0.2.5
BuildRequires:	libjpeg-devel
BuildRequires:	libopenraw-devel >= 0.0.5
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.14.0
BuildRequires:	libspiro-devel
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libv4l-devel
BuildRequires:	lua51-devel >= 5.1.0
BuildRequires:	pango-devel >= 1:1.10
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	ruby >= 1.9
%{?with_vala:BuildRequires:	vala}
Requires:	babl >= 0.1.6
Requires:	glib2 >= 1:2.28.0
Requires:	gdk-pixbuf2 >= 2.18.0
Requires:	jasper-libs >= 1.900.1
Requires:	lensfun >= 0.2.5
Requires:	libopenraw >= 0.0.5
Requires:	librsvg >= 1:2.14.0
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
Requires:	babl-devel >= 0.1.6
Requires:	glib2-devel >= 1:2.28.0

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

%package apidocs
Summary:	gegl library API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki gegl
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
gegl library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gegl.

%package -n vala-gegl
Summary:	Vala API for gegl library
Summary(pl.UTF-8):	API języka Vala dla biblioteki gegl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description -n vala-gegl
Vala API for gegl library.

%description -n vala-gegl -l pl.UTF-8
API języka Vala dla biblioteki gegl.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/umfpack" \
	--enable-docs%{!?with_doc:=no} \
	%{!?with_mmx:--disable-mmx} \
	%{!?with_sse:--disable-sse} \
	--disable-silent-rules \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gtkdochtmldir=%{_gtkdocdir}/gegl

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gegl-0.1/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gegl
%attr(755,root,root) %{_libdir}/libgegl-0.1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgegl-0.1.so.0
%{_libdir}/girepository-1.0/Gegl-0.1.typelib
%dir %{_libdir}/gegl-0.1
%attr(755,root,root) %{_libdir}/gegl-0.1/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgegl-0.1.so
%{_libdir}/libgegl-0.1.la
%{_includedir}/gegl-0.1
%{_datadir}/gir-1.0/Gegl-0.1.gir
%{_pkgconfigdir}/gegl.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgegl-0.1.a

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gegl
%endif

%if %{with vala}
%files -n vala-gegl
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gegl-0.1.vapi
%endif
