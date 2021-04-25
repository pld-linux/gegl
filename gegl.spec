#
# Conditional build:
%bcond_without	doc		# apidocs
%bcond_without	lua		# without lua support
%bcond_without	static_libs	# static library
%bcond_without	introspection	# API introspection
%bcond_without	vala		# Vala API

%if %{without introspection}
%undefine	with_vala
%endif

%ifarch x32
%undefine	with_lua
%endif

%define	babl_ver	0.1.78
%define	mrg_ver		0.1.4

Summary:	Generic image processing library
Summary(pl.UTF-8):	Ogólna biblioteka przetwarzania obrazu
Name:		gegl
Version:	0.4.30
Release:	2
License:	LGPL v3+/GPL v3+
Group:		Libraries
Source0:	https://download.gimp.org/pub/gegl/0.4/%{name}-%{version}.tar.xz
# Source0-md5:	6ae601b8c7cab8af5a36406df0b95ebf
Patch1:		%{name}-ruby1.9.patch
Patch2:		%{name}-build.patch
Patch3:		umfpack.patch
Patch4:		%{name}-link.patch
Patch5:		%{name}-no-lua.patch
URL:		https://www.gegl.org/
BuildRequires:	OpenEXR-devel >= 1.6.1
BuildRequires:	SDL2-devel >= 2.0.5
BuildRequires:	UMFPACK-devel
BuildRequires:	asciidoc
BuildRequires:	babl-devel >= %{babl_ver}
BuildRequires:	bash
BuildRequires:	cairo-devel >= 1.12.2
BuildRequires:	enscript
BuildRequires:	exiv2-devel >= 0.25
# libavcodec >= 55.69.100, libavformat >= 55.48.100, libavutil >= 55.92.100, libswscale >= 2.6.100
BuildRequires:	ffmpeg-devel >= 2.3
BuildRequires:	gcc >= 5:4.7
BuildRequires:	gdk-pixbuf2-devel >= 2.32.0
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	gexiv2-devel
BuildRequires:	glib2-devel >= 1:2.44.0
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 1.32.0}
BuildRequires:	graphviz
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	jasper-devel >= 1.900.1
BuildRequires:	json-glib-devel >= 1.2.6
BuildRequires:	lcms2-devel >= 2.8
BuildRequires:	lensfun-devel >= 0.2.5
BuildRequires:	libjpeg-devel >= 1.0.0
BuildRequires:	libnsgif-devel
BuildRequires:	libpng-devel >= 2:1.6.0
BuildRequires:	libraw-devel >= 0.15.4
BuildRequires:	librsvg-devel >= 1:2.40.6
BuildRequires:	libspiro-devel >= 0.5.0
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	libtiff-devel >= 4.0.0
BuildRequires:	libv4l-devel >= 1.0.1
BuildRequires:	libwebp-devel >= 0.5.0
%if %{with lua}
BuildRequires:	luajit-devel >= 2.0.4
BuildRequires:	lua51-devel >= 5.1.5-2
%endif
BuildRequires:	maxflow-devel >= 3.0.4
BuildRequires:	meson >= 0.50.0
BuildRequires:	mrg-devel >= %{mrg_ver}
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.38.0
BuildRequires:	perl-base >= 5
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.71.0
BuildRequires:	python3 >= 1:3.2
%if %{with introspection}
# for tests only
#BuildRequires:	python-pygobject3-devel >= 3.2.0
%endif
BuildRequires:	poly2tri-c-devel
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	ruby >= 1.9
BuildRequires:	tar >= 1:1.22
%if %{with vala}
BuildRequires:	vala >= 2:0.20.0
BuildRequires:	vala-babl >= %{babl_ver}
%endif
BuildRequires:	xz
BuildRequires:	zlib-devel >= 1.2.0
Requires:	OpenEXR >= 1.6.1
Requires:	SDL2 >= 2.0.5
Requires:	babl >= %{babl_ver}
Requires:	cairo >= 1.12.2
Requires:	gdk-pixbuf2 >= 2.32.0
Requires:	glib2 >= 1:2.44.0
Requires:	jasper-libs >= 1.900.1
Requires:	json-glib >= 1.2.6
Requires:	lcms2 >= 2.8
Requires:	lensfun >= 0.2.5
Requires:	libraw >= 0.15.4
Requires:	librsvg >= 1:2.40.6
Requires:	libspiro >= 0.5.0
Requires:	libtiff >= 4.0.0
Requires:	libwebp >= 0.5.0
Requires:	maxflow >= 3.0.4
Requires:	mrg-libs >= %{mrg_ver}
Requires:	pango >= 1:1.38.0
Requires:	poppler-glib >= 0.71.0
Requires:	zlib >= 1.2.0
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
Requires:	babl-devel >= %{babl_ver}
Requires:	glib2-devel >= 1:2.44.0
Requires:	json-glib-devel >= 1.2.6
Requires:	poly2tri-c-devel

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
BuildArch:	noarch

%description apidocs
gegl library API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki gegl.

%package -n vala-gegl
Summary:	Vala API for gegl library
Summary(pl.UTF-8):	API języka Vala dla biblioteki gegl
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
BuildArch:	noarch

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
%patch5 -p1

%build
CPPFLAGS="%{rpmcppflags} -I/usr/include/umfpack"
%meson build \
	%{?with_doc:-Ddocs=true} \
	%{!?with_introspection:-Dintrospection=false} \
	%{!?with_lua:-Dlua=disabled} \
	-Dworkshop=true

%ninja_build -C build

%if %{with doc}
rmdir build/docs/operations/RAM
# possible gegl-tester coredumps?
rm -f build/docs/operations/core*
%endif

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}-0.4

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}-0.4.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS
%attr(755,root,root) %{_bindir}/gegl
%attr(755,root,root) %{_bindir}/gegl-imgcmp
%attr(755,root,root) %{_libdir}/libgegl-0.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgegl-0.4.so.0
%attr(755,root,root) %{_libdir}/libgegl-npd-0.4.so
%attr(755,root,root) %{_libdir}/libgegl-sc-0.4.so
%{?with_introspection:%{_libdir}/girepository-1.0/Gegl-0.4.typelib}
%dir %{_libdir}/gegl-0.4
%attr(755,root,root) %{_libdir}/gegl-0.4/*.so
%{_libdir}/gegl-0.4/dropshadow2.json
%{_libdir}/gegl-0.4/grey2.json
%if %{with lua}
%dir %{_datadir}/gegl-0.4
%{_datadir}/gegl-0.4/lua
%endif

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
%doc build/docs/{operations,*.html,*.png}
%{_gtkdocdir}/gegl
%endif

%if %{with vala}
%files -n vala-gegl
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/gegl-0.4.deps
%{_datadir}/vala/vapi/gegl-0.4.vapi
%endif
