#
# Conditional build:
%bcond_without	static_libs	# static libraries
%bcond_without	fltk		# FLTK GUI tools (oyranos-config-fltk)
%bcond_without	qt		# Qt GUI tools (qscmevents)

Summary:	Colour Management System on operating system level
Summary(pl.UTF-8):	System zarządzania kolorami na poziomie systemu operacyjnego
Name:		oyranos
Version:	0.9.6
Release:	1
License:	BSD
Group:		Applications/Graphics
#Source0Download: https://github.com/oyranos-cms/oyranos/releases
Source0:	https://github.com/oyranos-cms/oyranos/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2a8c9783f762906ba7ff9ef43612041f
Patch0:		no-mesa10.patch
Patch1:		%{name}-libraw.patch
Patch2:		%{name}-exiv2.patch
Patch3:		%{name}-elektra.patch
Patch4:		%{name}-qt.patch
# not working currently (Aug 2023)
#URL:		http://www.oyranos.org/
URL:		https://github.com/oyranos-cms/oyranos
BuildRequires:	OpenICC-devel
BuildRequires:	cairo-devel
BuildRequires:	cmake >= 2.6.4
BuildRequires:	cups-devel
BuildRequires:	doxygen >= 1.5.8
BuildRequires:	elektra-devel >= 0.7
BuildRequires:	exiv2-devel
%if %{with fltk}
BuildRequires:	fltk-devel
BuildRequires:	fltk-fluid
BuildRequires:	fltk-gl-devel
%endif
BuildRequires:	gcc >= 6:4.2
BuildRequires:	gettext-tools
# not required for releases (generated code included)
#BuildRequires:	grantlee >= 0.2.0
BuildRequires:	lcms-devel
BuildRequires:	lcms2-devel
BuildRequires:	libXcm-devel >= 0.5.4
BuildRequires:	libgomp-devel
BuildRequires:	libltdl-devel
BuildRequires:	libpng-devel
BuildRequires:	libraw-devel >= 0.21
BuildRequires:	libtiff-devel
BuildRequires:	libxml2-devel >= 2
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sane-backends-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	yajl-devel
%if %{with qt}
BuildRequires:	Qt5Core-devel >= 5
BuildRequires:	Qt5Gui-devel >= 5
BuildRequires:	Qt5Widgets-devel >= 5
BuildRequires:	Qt5X11Extras-devel >= 5
BuildRequires:	Qt5Xml-devel >= 5
BuildRequires:	Qt5Svg-devel >= 5
BuildRequires:	qt5-build >= 5
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

%package module-sane
Summary:	SANE device support for Oyranos Colour Management System
Summary(pl.UTF-8):	Obsługa urządzeń SANE dla systemu zarządzania kolorami Oyranos
Group:		Applications/Graphics
Requires:	%{name} = %{version}-%{release}

%description module-sane
SANE device support for Oyranos Colour Management System.

%description module-sane -l pl.UTF-8
Obsługa urządzeń SANE dla systemu zarządzania kolorami Oyranos.

%package module-x11
Summary:	X11 and monitor support for Oyranos Colour Management System
Summary(pl.UTF-8):	Obsługa X11 i monitorów dla systemu zarządzania kolorami Oyranos
Group:		X11/Applications/Graphics
Requires:	%{name} = %{version}-%{release}
Requires:	xcalib

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
BuildArch:	noarch

%description apidocs
Oyranos API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API bibliotek Oyranos.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

# no reason to package also qt4 variant; qt5 one is enough
%{__sed} -i -e '/ADD_SUBDIRECTORY( qt4 )/d' src/tools/qcmsevents/CMakeLists.txt

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# qt4 version not built
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/qcmsevents-qt4.1*
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS.md COPYING.md ChangeLog.md README.md
%attr(755,root,root) %{_bindir}/oyranos-compat-gnome
%attr(755,root,root) %{_bindir}/oyranos-icc
%attr(755,root,root) %{_bindir}/oyranos-policy
%attr(755,root,root) %{_bindir}/oyranos-profile
%attr(755,root,root) %{_bindir}/oyranos-profile-install
%attr(755,root,root) %{_bindir}/oyranos-profiles
%attr(755,root,root) %{_bindir}/oyranos-xforms
%attr(755,root,root) %{_bindir}/oyranos-xforms-modules
%dir %{_libdir}/color
%dir %{_libdir}/color/modules
# R: elektra-libs
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_elDB_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_lcm2_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_lcms_cmm_module.so
# R: libraw
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_lraw_cmm_module.so
# R: libjpeg
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oJPG_cmm_module.so
# R: libpng
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oPNG_cmm_module.so
# R: yajl
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oiDB_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oicc_cmm_module.so
# R: libraw
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oyRE_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oyra_cmm_module.so
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_trds_cmm_module.so
%dir %{_libdir}/oyranos-meta
%attr(755,root,root) %{_libdir}/oyranos-meta/liboyranos_oyIM_cmm_module.so
%dir %{_datadir}/color/rank-map
%{_datadir}/color/rank-map/config.icc_profile.raw-image.oyRE.json
%dir %{_datadir}/color/settings
%{_datadir}/color/settings/*.policy.xml
%{_desktopdir}/oyranos-profile-install.desktop
%{_pixmapsdir}/lcms_logo2.png
%{_pixmapsdir}/oyranos_logo.png
%{_mandir}/man1/oyranos-policy.1*
%{_mandir}/man1/oyranos-profile.1*
%{_mandir}/man1/oyranos-profile-install.1*
%{_mandir}/man1/oyranos-profiles.1*
%{_mandir}/man1/oyranos-xforms.1*
%{_mandir}/man1/oyranos-xforms-modules.1*

%files module-cups
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_CUPS_cmm_module.so
%{_datadir}/color/rank-map/config.icc_profile.printer.CUPS.json

%files module-sane
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_SANE_cmm_module.so
%{_datadir}/color/rank-map/config.icc_profile.scanner.SANE.json

%files module-x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oyranos-monitor
%attr(755,root,root) %{_bindir}/oyranos-monitor-daemon
# R: libX11 libXfixes libXinerama libXrandr libXxf86vm libXcm
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oyX1_cmm_module.so
# R: libXfixes libXcm
%attr(755,root,root) %{_libdir}/color/modules/liboyranos_oydi_cmm_module.so
%{_datadir}/color/rank-map/config.icc_profile.monitor.oyX1.qarz.json
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
%attr(755,root,root) %{_bindir}/oyranos-image-display
%attr(755,root,root) %{_bindir}/oyranos-xforms-fltk
%{_desktopdir}/oyranos-image-display.desktop
%{_mandir}/man1/oyranos-config-fltk.1*
%{_mandir}/man1/oyranos-image-display.1*
%{_mandir}/man1/oyranos-xforms-fltk.1*
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
%attr(755,root,root) %{_libdir}/libOyranos.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOyranos.so.0
%attr(755,root,root) %{_libdir}/libOyranosConfig.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOyranosConfig.so.0
%attr(755,root,root) %{_libdir}/libOyranosCore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOyranosCore.so.0
%attr(755,root,root) %{_libdir}/libOyranosModules.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOyranosModules.so.0
%attr(755,root,root) %{_libdir}/libOyranosObject.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libOyranosObject.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/oyranos-config
%attr(755,root,root) %{_libdir}/libOyranos.so
%attr(755,root,root) %{_libdir}/libOyranosConfig.so
%attr(755,root,root) %{_libdir}/libOyranosCore.so
%attr(755,root,root) %{_libdir}/libOyranosModules.so
%attr(755,root,root) %{_libdir}/libOyranosObject.so
%{_libdir}/cmake/oyranos
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
