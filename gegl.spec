#
# Conditional build:
%bcond_with	mmx		# use MMX instructions
%bcond_with	sse		# use SSE instructions
%bcond_without	doc		# apidocs
# reenable when new babl will arrive that actually is able to build
%bcond_with	introspection	# API introspection
# reenable when new babl will arrive that actually is able to build
%bcond_with	vala		# Vala API

%ifarch %{x8664} athlon pentium3 pentium4
%define	with_mmx	1
%endif
%ifarch %{x8664} pentium3 pentium4
%define	with_sse	1
%endif
%if %{without introspection}
%undefine	with_vala
%endif
Summary:	Generic image processing library
Summary(pl.UTF-8):	Ogólna biblioteka przetwarzania obrazu
Name:		gegl
Version:	0.2.0
Release:	7
License:	LGPL v3+
Group:		Libraries
Source0:	ftp://ftp.gimp.org/pub/gegl/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	32b00002f1f1e316115c4ed922e1dec8
Patch0:		%{name}-lua.patch
Patch1:		%{name}-ffmpeg.patch
Patch2:		%{name}-ruby1.9.patch
Patch3:		%{name}-build.patch
Patch4:		%{name}-introspection.patch
URL:		http://www.gegl.org/
%{?with_introspection:BuildRequires:	/usr/share/gir-1.0/Babl-0.1.gir}
BuildRequires:	OpenEXR-devel
BuildRequires:	SDL-devel
BuildRequires:	UMFPACK-devel
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.11
BuildRequires:	babl-devel >= 0.1.10
BuildRequires:	cairo-devel
BuildRequires:	enscript
BuildRequires:	exiv2-devel
BuildRequires:	ffmpeg-devel >= 0.8
BuildRequires:	gdk-pixbuf2-devel >= 2.18.0
BuildRequires:	glib2-devel >= 1:2.28.0
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 0.10.0}
BuildRequires:	graphviz
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.40.1
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
Requires:	babl >= 0.1.10
Requires:	gdk-pixbuf2 >= 2.18.0
Requires:	glib2 >= 1:2.28.0
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
Requires:	babl-devel >= 0.1.10
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

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
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CPPFLAGS="%{rpmcppflags} -I/usr/include/umfpack" \
	--enable-docs%{!?with_doc:=no} \
	%{?with_introspection:--enable-introspection} \
	%{!?with_mmx:--disable-mmx} \
	%{!?with_sse:--disable-sse} \
	--disable-silent-rules \
	--enable-static \
	--with%{!?with_vala:out}-vala
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gtkdochtmldir=%{_gtkdocdir}/gegl

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gegl-0.2/*.{a,la}

%find_lang %{name}-0.2

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-0.2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gegl
%attr(755,root,root) %{_libdir}/libgegl-0.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgegl-0.2.so.0
%{?with_introspection:%{_libdir}/girepository-1.0/Gegl-0.2.typelib}
%dir %{_libdir}/gegl-0.2
%attr(755,root,root) %{_libdir}/gegl-0.2/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgegl-0.2.so
%{_libdir}/libgegl-0.2.la
%{_includedir}/gegl-0.2
%{?with_introspection:%{_datadir}/gir-1.0/Gegl-0.2.gir}
%{_pkgconfigdir}/gegl-0.2.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgegl-0.2.a

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gegl
%endif

%if %{with vala}
%files -n vala-gegl
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gegl-0.2.vapi
%endif
