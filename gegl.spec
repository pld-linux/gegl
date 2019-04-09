#
# Conditional build:
%bcond_with	mmx		# use MMX instructions
%bcond_with	sse		# use SSE instructions
%bcond_without	doc		# apidocs
%bcond_without	static_libs	# static library
%bcond_without	introspection	# API introspection
%bcond_without	vala		# Vala API

%ifarch %{x8664} athlon pentium3 pentium4
%define	with_mmx	1
%endif
%ifarch %{x8664} pentium3 pentium4
%define	with_sse	1
%endif
%if %{without introspection}
%undefine	with_vala
%endif

%define	babl_version	0.1.62
%define	mrg_version	0.1.2-1.20190322.1

Summary:	Generic image processing library
Summary(pl.UTF-8):	Ogólna biblioteka przetwarzania obrazu
Name:		gegl
Version:	0.4.14
Release:	1
License:	LGPL v3+
Group:		Libraries
Source0:	https://download.gimp.org/pub/gegl/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	88004f3a204e2506cd0cc445eba8d63e
Patch1:		%{name}-ruby1.9.patch
Patch2:		%{name}-build.patch
Patch3:		umfpack.patch
Patch4:		%{name}-Wformat-security.patch
URL:		http://www.gegl.org/
BuildRequires:	OpenEXR-devel >= 1.6.1
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	UMFPACK-devel
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.11
BuildRequires:	babl-devel >= %{babl_version}
BuildRequires:	cairo-devel >= 1.12.2
BuildRequires:	enscript
BuildRequires:	exiv2-devel >= 0.25
# libavformat >= 55.48.100, libavcodec >= 55.69.100, libswscale >= 2.6.100
BuildRequires:	ffmpeg-devel >= 2.3
BuildRequires:	gdk-pixbuf2-devel >= 2.32.0
BuildRequires:	gettext-tools
BuildRequires:	gexiv2-devel
BuildRequires:	glib2-devel >= 1:2.44.0
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 1.32.0}
BuildRequires:	graphviz
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	intltool >= 0.40.1
BuildRequires:	jasper-devel >= 1.900.1
BuildRequires:	json-glib-devel
BuildRequires:	lcms2-devel >= 2.8
BuildRequires:	lensfun-devel >= 0.2.5
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libraw-devel >= 0.15.4
BuildRequires:	librsvg-devel >= 1:2.40.6
BuildRequires:	libspiro-devel
BuildRequires:	libtiff-devel >= 4.0.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	libv4l-devel >= 1.0.1
BuildRequires:	libwebp-devel >= 0.5.0
BuildRequires:	luajit-devel >= 2.0.4
BuildRequires:	lua51-devel >= 5.1.5-2
BuildRequires:	mrg-devel >= %{mrg_version}
BuildRequires:	pango-devel >= 1:1.38.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.71.0
BuildRequires:	python >= 1:2.5.0
# either one?
#BuildRequires:	python-pygobject-devel >= 2.26
BuildRequires:	python-pygobject3-devel >= 3.2
BuildRequires:	poly2tri-c-devel
BuildRequires:	ruby >= 1.9
%{?with_vala:BuildRequires:	vala >= 2:0.20.0}
Requires:	babl >= %{babl_version}
Requires:	gdk-pixbuf2 >= 2.32.0
Requires:	glib2 >= 1:2.44.0
Requires:	jasper-libs >= 1.900.1
Requires:	lensfun >= 0.2.5
Requires:	libraw >= 0.15.4
Requires:	librsvg >= 1:2.40.6
Requires:	libtiff >= 4.0.0
Requires:	mrg-libs >= %{mrg_version}
Requires:	pango >= 1:1.38.0
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
Requires:	babl-devel >= %{babl_version}
Requires:	glib2-devel >= 1:2.44.0

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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n vala-gegl
Vala API for gegl library.

%description -n vala-gegl -l pl.UTF-8
API języka Vala dla biblioteki gegl.

%prep
%setup -q
%patch1 -p1
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
	%{?with_static_libs:--enable-static} \
	--with-vala%{!?with_vala:=no}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gtkdochtmldir=%{_gtkdocdir}/gegl

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libgegl*-0.4.la
# dlopened modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gegl-0.4/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gegl-0.4/*.a
%endif

%find_lang %{name}-0.4

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-0.4.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gcut
%attr(755,root,root) %{_bindir}/gegl
%attr(755,root,root) %{_bindir}/gegl-imgcmp
%attr(755,root,root) %{_libdir}/libgegl-0.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgegl-0.4.so.0
%attr(755,root,root) %{_libdir}/libgegl-npd-0.4.so
%attr(755,root,root) %{_libdir}/libgegl-sc-0.4.so
%{?with_introspection:%{_libdir}/girepository-1.0/Gegl-0.4.typelib}
%dir %{_libdir}/gegl-0.4
%attr(755,root,root) %{_libdir}/gegl-0.4/*.so
%{_libdir}/gegl-0.4/grey2.json

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgegl-0.4.so
%{_includedir}/gegl-0.4
%{?with_introspection:%{_datadir}/gir-1.0/Gegl-0.4.gir}
%{_pkgconfigdir}/gegl-0.4.pc
%{_pkgconfigdir}/gegl-sc-0.4.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgegl-0.4.a
%{_libdir}/libgegl-npd-0.4.a
%{_libdir}/libgegl-sc-0.4.a
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gegl
%endif

%if %{with vala}
%files -n vala-gegl
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gegl-0.4.deps
%{_datadir}/vala/vapi/gegl-0.4.vapi
%endif
