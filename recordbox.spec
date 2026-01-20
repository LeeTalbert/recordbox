%global debug_package %{nil}

Name:		recordbox
Version:	0.10.4
Release:	1
Source0:	https://codeberg.org/edestcroix/Recordbox/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Recordbox is yet another music player for Linux, built with GTK and Libadwaita for the GNOME desktop
URL:		https://codeberg.org/edestcroix/Recordbox
License:	GPLv3
Group:		Sound/Players

BuildSystem:	meson

BuildRequires:	rust-packaging
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	gio2.0-64
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	gstreamer1.0-decoders-audio

%description
%{summary}.

%prep
%autosetup -p1 -n %{name}

%files
