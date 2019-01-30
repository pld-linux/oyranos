#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
%bcond_without	fltk		# FLTK GUI tools (oyranos-config-fltk)
%bcond_without	qt		# Qt GUI tools (qscmevents)

Summary:	Colour Management System on operating system level
Summary(pl.UTF-8):	System zarządzania kolorami na poziomie systemu operacyjnego
Name:		oyranos
Version:	0.9.5
Release:	9
License:	BSD
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/oyranos/%{name}-%{version}.tar.bz2
# Source0-md5:	f59ef03182597e1e7ba0e434599eb0c4
Patch0:		no-mesa10.patch
URL:		http://www.oyranos.org/
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 2.6.4
BuildRequires:	cups-devel
BuildRequires:	doxygen
BuildRequires:	elektra-devel >= 0.7
BuildRequires:	exiv2-devel
%if %{with fltk}
BuildRequires:	fltk-devel
BuildRequires:	fltk-gl-devel
%endif
BuildRequires:	gcc >= 6:4.2
BuildRequires:	gettext-tools
# not required for releases (generated code included)
#BuildRequires:	grantlee >= 0.2.0
BuildRequires:	lcms-devel
BuildRequires:	lcms2-devel
BuildRequires:	libXcm-devel
BuildRequires:	libgomp-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	libraw-devel
BuildRequires:	libxml2-devel >= 2
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	yajl-devel
%if %{with qt}
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	qt4-build >= 4
%endif
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Oyranos is a Colour Management System (CMS) on operating system level.
It allows to match predictably input device colours to output device
colours across supporting applications. One goal is to make colour
management useful for all users in a automated fashion and regardless
of any technical knowledge.

%description -l pl.UTF-8
Oyranos to system zarządzania kolorami (CMS - Colour Management
System) na poziomie systemu operacyjnego. Pozwala na przewidywalne
powiązanie kolorów urządzeń wejściowych z kolorami urządzeń
wyjściowych poprzez wszystkie aplikacje obsługujące ten system. Celem
jest uprzystępnienie zarządzania kolorami dla wszystkich użytkowników
w sposób zautomatyzowany, niezależny od wiedzy technicznej.

%package module-cups
Summary:	CUPS device support for Oyranos Colour Management System
Summary(pl.UTF-8):	Obsługa urządzeń CUPS dla systemu zarządzania kolorami Oyranos
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description module-cups
CUPS device support for Oyranos Colour Management System.

%description module-cups -l pl.UTF-8
Obsługa urządzeń CUPS dla systemu zarządzania kolorami Oyranos.

%package module-x11
Summary:	X11 and monitor support for Oyranos Colour Management System
Summary(pl.UTF-8):	Obsługa X11 i monitorów dla systemu zarządzania kolorami Oyranos
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description module-x11
X11 and monitor support for Oyranos Colour Management System.

%description module-x11 -l pl.UTF-8
Obsługa X11 i monitorów dla systemu zarządzania kolorami Oyranos.

%package profile-graph
Summary:	Profile 2D graph tool
Summary(pl.UTF-8):	Narzędzie do rysowania dwuwymiarowych wykresów profili
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description profile-graph
The grapher renders a simple gamut hull of a ICC profile in 2D.

%description profile-graph -l pl.UTF-8
Program rysujący w dwóch wymiarach prosty obraz gamy kolorów z profilu
ICC.

%package ui-fltk
Summary:	FLTK-based GUI for Oyranos Colour Management System
Summary(pl.UTF-8):	Oparty na FLTK graficzny interfejs dla systemu zarządzania kolorami Oyranos
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description ui-fltk
FLTK-based configuration GUI for Oyranos Colour Management System.

%description ui-fltk -l pl.UTF-8
Oparty na FLTK graficzny interfejs konfiguracyjny do systemu
zarządzania kolorami Oyranos.

%package ui-qt
Summary:	Qt-based GUI for Oyranos Colour Management System
Summary(pl.UTF-8):	Oparty na Qt graficzny interfejs dla systemu zarządzania kolorami Oyranos
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description ui-qt
Qt-based applet showing state of Oyranos Colour Management System.

%description ui-qt -l pl.UTF-8
Oparty na Qt aplet pokazyjący stan systemu zarządzania kolorami
Oyranos.

%package libs
Summary:	Oyranos Colour Management System libraries
Summary(pl.UTF-8):	Biblioteki systemu zarządzania kolorami Oyranos
Group:		Libraries
Requires:	elektra-libs >= 0.7

%description libs
Oyranos Colour Management System libraries.

%description libs -l pl.UTF-8
Biblioteki systemu zarządzania kolorami Oyranos.

%package devel
Summary:	Header files for oyranos libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek oyranos
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for oyranos libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek oyranos.

%package static
Summary:	Static oyranos libraries
Summary(pl.UTF-8):	Statyczne biblioteki oyranos
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static oyranos libraries.

%description static -l pl.UTF-8
Statyczne biblioteki oyranos.

%package apidocs
Summary:	Oyranos API documentation
Summary(pl.UTF-8):	Dokumentacja API bibliotek Oyranos
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Oyranos API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek Oyranos.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/oyranos/html

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/oyranos-icc
%attr(755,root,root) %{_bindir}/oyranos-policy
%attr(755,root,root) %{_bindir}/oyranos-profile
%attr(755,root,root) %{_bindir}/oyranos-profile-install
%attr(755,root,root) %{_bindir}/oyranos-profiles
%attr(755,root,root) %{_bindir}/oyranos-xforms-modules
%dir %{_libdir}/color
%dir %{_libdir}/color/modules
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_lcm2_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_lcms_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_lraw_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oPNG_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oicc_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oyRE_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oyra_cmm_module.so
%attr(755,root,root) %{_libdir}/oyranos/liboyranos_oyIM_cmm_module.so
%dir %{_datadir}/color/settings
%{_datadir}/color/settings/*.policy.xml
%{_desktopdir}/oyranos-profile-install.desktop
%{_pixmapsdir}/lcms_logo2.png
%{_pixmapsdir}/oyranos_logo.png
%{_mandir}/man1/oyranos-policy.1*
%{_mandir}/man1/oyranos-profile.1*
%{_mandir}/man1/oyranos-profile-install.1*
%{_mandir}/man1/oyranos-profiles.1*
%{_mandir}/man1/oyranos-xforms-modules.1*

%files module-cups
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_CUPS_cmm_module.so

%files module-x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oyranos-monitor
%attr(755,root,root) %{_bindir}/oyranos-monitor-daemon
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oyX1_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oydi_cmm_module.so
/etc/xdg/autostart/oyranos-monitor-setup.desktop
%{_mandir}/man1/oyranos-monitor.1*
%{_mandir}/man1/oyranos-monitor-daemon.1*

%files profile-graph
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oyranos-profile-graph
%{_mandir}/man1/oyranos-profile-graph.1*

%if %{with fltk}
%files ui-fltk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oyranos-config-fltk
%{_mandir}/man1/oyranos-config-fltk.1*
%endif

%if %{with qt}
%files ui-qt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qcmsevents
%{_desktopdir}/qcmsevents-applet.desktop
%{_pixmapsdir}/qcmsevents.svg
%{_mandir}/man1/qcmsevents.1*
%endif

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liboyranos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboyranos.so.0
%attr(755,root,root) %{_libdir}/liboyranos_config.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboyranos_config.so.0
%attr(755,root,root) %{_libdir}/liboyranos_core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboyranos_core.so.0
%attr(755,root,root) %{_libdir}/liboyranos_modules.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboyranos_modules.so.0
%attr(755,root,root) %{_libdir}/liboyranos_object.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liboyranos_object.so.0
# used by both base and -devel
%dir %{_libdir}/oyranos

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oyranos-config
%attr(755,root,root) %{_libdir}/liboyranos.so
%attr(755,root,root) %{_libdir}/liboyranos_config.so
%attr(755,root,root) %{_libdir}/liboyranos_core.so
%attr(755,root,root) %{_libdir}/liboyranos_modules.so
%attr(755,root,root) %{_libdir}/liboyranos_object.so
%{_libdir}/oyranos/cmake
%{_includedir}/oyranos
%{_pkgconfigdir}/oyranos.pc
%{_mandir}/man3/oyranos-config.3*
%{_mandir}/man3/oyranos.3*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/liboyranos-static.a
%{_libdir}/liboyranos_config-static.a
%{_libdir}/liboyranos_core-static.a
%{_libdir}/liboyranos_modules-static.a
%{_libdir}/liboyranos_object-static.a
%endif

%files apidocs
%defattr(644,root,root,755)
%doc build/doc/html/*.{css,html,js,png}
