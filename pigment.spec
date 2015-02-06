%define		api	0.3
%define		major		11
%define		libname		%mklibname %{name} %{api} %{major}
%define		develname	%mklibname %{name} -d

Summary:	User interface library with embedded multimedia
Name:		pigment
Version:	0.3.17
Release:	6
License:	LGPLv2+
Group:		Development/C
URL:		https://code.fluendo.com/pigment/trac
Source0:	http://elisa.fluendo.com/static/download/pigment/%{name}-%{version}.tar.bz2
Patch0:		pigment-0.3.17-redefinition.patch
Patch1:		pigment-0.3.17-gleslib.patch
Patch2:		pigment-0.3.17-install.patch
BuildRequires:	pkgconfig(cairo) >= 1.4
BuildRequires:	pkgconfig(cairo-xlib)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.8.0
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-0.10) >= 0.10.0
BuildRequires:	pkgconfig(gstreamer-base-0.10) >= 0.10.0
BuildRequires:	pkgconfig(gstreamer-check-0.10)  >= 0.10.0
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)  >= 0.10.0
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(pango) >= 1.20
BuildRequires:	pkgconfig(pangocairo) >= 1.20
BuildRequires:	pkgconfig(tslib-0.0)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	gtk-doc

%description
Pigment is a library designed to easily build user interfaces
with embedded multimedia. Its design allows to use it on several
platforms, thanks to a plugin system allowing to choose the underlying
graphical API. Pigment is the rendering engine of Elisa, the Fluendo
Media Center project.

%package -n %{libname}
Group:		System/Libraries
Summary:	Shared library of Pigment

%description -n %{libname}
Pigment is a library designed to easily build user interfaces
with embedded multimedia. Its design allows to use it on several
platforms, thanks to a plugin system allowing to choose the underlying
graphical API. Pigment is the rendering engine of Elisa, the Fluendo
Media Center project.

%package -n %{develname}
Group:		Development/C
Summary:	Development headers for shared library of Pigment
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Pigment is a library designed to easily build user interfaces
with embedded multimedia. Its design allows to use it on several
platforms, thanks to a plugin system allowing to choose the underlying
graphical API. Pigment is the rendering engine of Elisa, the Fluendo
Media Center project.

%prep
%setup -q
%patch0 -p2
%patch1 -p1
%patch2 -p1

%build
autoreconf -fi
%configure2_5x --disable-gtk-doc --disable-static
%make

%install
%makeinstall_std

%files
%dir %{_libdir}/%{name}-%{api}/%{version}
%{_libdir}/%{name}-%{api}/%{version}/*.so
%{_datadir}/gtk-doc/html/%{name}

%files -n %{libname}
%{_libdir}/lib*-%{api}.so.%{major}
%{_libdir}/lib*-%{api}.so.%{major}.*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc


