%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
#define commit cc1ac2462e41873741c8b6f3fcafa29ae3ce6a30

Name:		plasma6-tokodon
Version:	24.08.1
Release:	%{?git:0.%{git}.}1
Summary:	Mastodon client for Plasma Mobile
%if 0%{?git}
Source0:	https://invent.kde.org/network/tokodon/-/archive/%{gitbranch}/tokodon-%{gitbranchd}.tar.bz2#/tokodon-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/tokodon-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)
BuildRequires:	cmake(Qt6WebSockets)
BuildRequires:	cmake(Qt6WebView)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Sonnet)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6QQC2DesktopStyle)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6KIO)
BuildRequires:	cmake(KF6Purpose)
BuildRequires:	cmake(MpvQt)
BuildRequires:  qt6-qtbase-theme-gtk3

%description
Mastodon client for Plasma Mobile

%prep
%autosetup -p1 -n tokodon-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang tokodon

%files -f tokodon.lang
%{_bindir}/tokodon
%{_bindir}/tokodon-offline
%{_datadir}/applications/org.kde.tokodon.desktop
%{_datadir}/metainfo/org.kde.tokodon.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.tokodon.svg
%{_datadir}/icons/hicolor/scalable/actions/tokodon-*.svg
%{_datadir}/knotifications6/tokodon.notifyrc
%{_datadir}/qlogging-categories6/tokodon.categories
%{_qtdir}/plugins/kf6/purpose/tokodonplugin.so
