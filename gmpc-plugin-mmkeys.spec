%define		source_name gmpc-mmkeys
Summary:	Gnome Music Player Client Multimedia Keys plugin
Name:		gmpc-plugin-mmkeys
Version:	11.8.16
Release:	1
License:	GPL v3
Group:		X11/Applications/Sound
Source0:	http://download.sarine.nl/Programs/gmpc/%{version}/%{source_name}-%{version}.tar.gz
# Source0-md5:	a66e9cd02addafedd91fa5de8aa8e824
URL:		http://gmpc.wikia.com/wiki/GMPC_PLUGIN_MMKEYS
BuildRequires:	autoconf >= 2.58
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel >= 1:2.16
BuildRequires:	gmpc-devel >= 0.18.1
BuildRequires:	gtk+2-devel >= 2:2.12
BuildRequires:	libmpd-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	vala >= 0.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gnome Music Player Client Multimedia Keys plugin.

%prep
%setup -qn %{source_name}-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gmpc/plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gmpc/plugins/mmkeysplugin.so
