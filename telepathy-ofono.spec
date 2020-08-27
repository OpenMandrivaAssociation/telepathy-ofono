%define snapshot 20200827

Summary:	ofono telephone services for telepathy
Name:		telepathy-ofono
Version:	0.1
Release:	%{?snapshot:0.%{snapshot}.}1
Source0:	https://github.com/TelepathyIM/telepathy-ofono/archive/staging/%{name}-%{snapshot}.tar.gz
Patch0:		telepathy-ofono-no-underlinking.patch
License:	LGPLv3
Group:		Networking/Instant messaging
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	pkgconfig(TelepathyQt5)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(mission-control-plugins)
BuildRequires:	pkgconfig(ofono-qt)
BuildRequires:	%{_lib}phonenumber-devel

%description
ofono telephone services for telepathy

%prep
%autosetup -p1 -n %{name}-staging
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_libdir}/mission-control-plugins.0/mcp-account-manager-ofono.so
%{_libexecdir}/telepathy-ofono
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.ofono.service
%{_datadir}/telepathy/managers/ofono.manager
