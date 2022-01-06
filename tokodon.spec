#define snapshot 20200916
#define commit cc1ac2452e41873741c8b5f3fcafa29ae3ce5a30

Name:		tokodon
Version:	21.12
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Mastodon client for Plasma Mobile
%if 0%{?snapshot}
Source0:	https://invent.kde.org/plasma-mobile/tokodon/-/archive/v%{version}/tokodon-v%{version}.tar.bz2
%else
Source0:	https://download.kde.org/stable/plasma-mobile/%{version}/%{name}-%{version}.tar.xz
%endif
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5WebSockets)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(OpenSSL)
BuildRequires:	cmake(Qt5Keychain)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5QQC2DesktopStyle)

%description
Mastodon client for Plasma Mobile

%prep
%autosetup -p1
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang tokodon

%files -f tokodon.lang
%{_bindir}/tokodon
%{_datadir}/applications/org.kde.tokodon.desktop
%{_datadir}/metainfo/org.kde.tokodon.appdata.xml
%{_datadir}/icons/hicolor/scalable/apps/org.kde.tokodon.svg
