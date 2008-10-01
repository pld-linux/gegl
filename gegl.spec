#
# Conditional build:
%bcond_with	mmx	# use MMX instructions
%bcond_with	sse	# use SSE instructions
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
Version:	0.0.18
Release:	3
License:	LGPL v3+
Group:		Libraries
Source0:	ftp://ftp.gtk.org/pub/gegl/0.0/%{name}-%{version}.tar.bz2
# Source0-md5:	e458409440a7b51f446df321c3657e4d
Patch0:		%{name}-lua.patch
Patch1:		%{name}-ffmpeg.patch
URL:		http://www.gegl.org/
BuildRequires:	OpenEXR-devel
BuildRequires:	SDL-devel
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	babl-devel >= 0.0.22
BuildRequires:	cairo-devel
BuildRequires:	enscript
BuildRequires:	ffmpeg-devel
BuildRequires:	glib2-devel >= 1:2.14.1
BuildRequires:	graphviz
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-doc
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel >= 1:2.14.0
BuildRequires:	libtool
BuildRequires:	lua51-devel >= 5.1.0
BuildRequires:	pango-devel >= 1:1.10
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
Requires:	babl-devel >= 0.0.20
Requires:	glib2-devel >= 1:2.14.1

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_mmx:--disable-mmx} \
	%{!?with_sse:--disable-sse} \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	help_dir=$RPM_BUILD_ROOT%{_gtkdocdir}/gegl

rm -f $RPM_BUILD_ROOT%{_libdir}/gegl-0.0/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gegl
%attr(755,root,root) %{_libdir}/libgegl-0.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgegl-0.0.so.0
%dir %{_libdir}/gegl-0.0
%attr(755,root,root) %{_libdir}/gegl-0.0/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgegl-0.0.so
%{_libdir}/libgegl-0.0.la
%{_includedir}/gegl-0.0
%{_pkgconfigdir}/gegl.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgegl-0.0.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gegl
