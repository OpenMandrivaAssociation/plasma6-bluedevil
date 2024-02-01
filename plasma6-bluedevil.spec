%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20231103

Summary:	The bluetooth stack for KDE 6
Name:		plasma6-bluedevil
Version:	5.93.0
Release:	%{?git:0.%{git}.}1
Group:		Graphical desktop/KDE
License:	GPL
Url:		https://projects.kde.org/projects/extragear/base/bluedevil
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/bluedevil/-/archive/master/bluedevil-master.tar.bz2#/bluedevil-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/plasma/%(echo %{version} |cut -d. -f1-3)/bluedevil-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6BluezQt)
BuildRequires:	cmake(Plasma) >= 5.90.0
BuildRequires:	cmake(PlasmaQuick)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:	cmake(KF6KDED)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	cmake(KF6Svg)
BuildRequires:	pkgconfig(shared-mime-info)
Provides:	bluez-pin
Requires:	bluez >= 4.28
Requires:	obexd

%description
BlueDevil is the new bluetooth stack for KDE, it's composed of:
KCM, KDED, KIO, Library and some other small applications.

%files -f %{name}.lang
%{_bindir}/*
%{_qtdir}/plugins/kf6/kio/*.so
%{_datadir}/applications/*
%{_datadir}/bluedevilwizard
%{_datadir}/knotifications6/*
%{_datadir}/mime/packages/bluedevil-mime.xml
%{_datadir}/metainfo/org.kde.plasma.bluetooth.appdata.xml

%{_qtdir}/plugins/plasma/kcms/systemsettings/kcm_bluetooth.so
%{_datadir}/qlogging-categories6/bluedevil.categories

%dir %{_qtdir}/qml/org/kde/plasma/private/bluetooth
%{_qtdir}/plugins/kf6/kded/*.so
%{_qtdir}/qml/org/kde/plasma/private/bluetooth/libbluetoothplugin.so
%{_qtdir}/qml/org/kde/plasma/private/bluetooth/qmldir
%{_qtdir}/qml/org/kde/plasma/private/bluetooth/bluetoothplugin.qmltypes
%{_qtdir}/qml/org/kde/plasma/private/bluetooth/kde-qmlmodule.version

%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/metadata.json
%{_datadir}/plasma/plasmoids/org.kde.plasma.bluetooth/contents/ui/*.qml
%{_datadir}/remoteview/bluetooth-network.desktop

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n bluedevil-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
