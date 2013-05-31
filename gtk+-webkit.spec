Summary:	Port of WebKit embeddable web component to GTK+
Name:		gtk+-webkit
Version:	2.0.2
Release:	1
License:	BSD-like
Group:		X11/Libraries
Source0:	http://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
# Source0-md5:	a4024f4b33d829ec1034179e94f9cab6
URL:		http://www.webkitgtk.org/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	curl-devel
BuildRequires:	enchant-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	geoclue-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gperf
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	icu-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	libsoup-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxslt-devel
BuildRequires:	pkg-config
BuildRequires:	ruby
BuildRequires:	sqlite3-devel
BuildRequires:	xorg-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
webkit is a port of the WebKit embeddable web component to GTK+.

%package devel
Summary:	Development files for webkit
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for webkit.

%prep
%setup -qn webkitgtk-%{version}

%build
%{__libtoolize}
%{__aclocal} -I Source/autotools
%{__autoheader}
%{__automake}
%{__autoconf}
# https://bugs.webkit.org/show_bug.cgi?id=91154
export CFLAGS="%(echo %{rpmcflags} | sed 's/ -g2/ -g1/g')"
export CXXFLAGS="%(echo %{rpmcxxflags} | sed 's/ -g2/ -g1/g')"
%configure \
	--disable-webkit2	\
	--enable-geolocation	\
	--enable-introspection	\
	--enable-spellcheck	\
	--with-gstreamer=1.0	\
	--with-gtk=2.0
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang WebKitGTK-2.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f WebKitGTK-2.0.lang
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libjavascriptcoregtk-*.so.?
%attr(755,root,root) %ghost %{_libdir}/libwebkitgtk-*.so.?
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libwebkitgtk-*.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib
%{_datadir}/webkitgtk-*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jsc-1
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/webkitgtk-1.0
%{_pkgconfigdir}/*.pc
%{_datadir}/gir-1.0/*.gir

