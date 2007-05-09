%define name pigment
%define version 0.1.5
%define release %mkrel 1
%define major 0
%define libname %mklibname %name %major

Summary: Python user interface library with embedded multimedia
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://elisa.fluendo.com/static/download/pigment/%{name}-%{version}.tar.bz2
License: GPL
Group: Development/Python
Url: https://core.fluendo.com/pigment/trac
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: automake
BuildRequires: libx11-devel
BuildRequires: libxrandr-devel
BuildRequires: gtk-doc
BuildRequires: libgstreamer0.10-devel
BuildRequires: libgstreamer0.10-plugins-base-devel
BuildRequires: gstreamer0.10-python
BuildRequires: glib2-devel
BuildRequires: gdk-pixbuf-devel
BuildRequires: cairo-devel
BuildRequires: mesaglu-devel
BuildRequires: python-devel
BuildRequires: python-gobject
BuildRequires: pygtk2.0-devel

%description
Pigment is a Python library designed to easily build user interfaces 
with embedded multimedia. Its design allows to use it on several 
platforms, thanks to a plugin system allowing to choose the underlying 
graphical API. Pigment is the rendering engine of Elisa, the Fluendo 
Media Center project.

%package devel
Group: Development/Python
Summary: Development headers for Pigment

%description devel
Pigment is a Python library designed to easily build user interfaces 
with embedded multimedia. Its design allows to use it on several 
platforms, thanks to a plugin system allowing to choose the underlying 
graphical API. Pigment is the rendering engine of Elisa, the Fluendo 
Media Center project.

%package -n %libname
Group: System/Libraries
Summary: Shared library of Pigment

%description -n %libname
Pigment is a Python library designed to easily build user interfaces 
with embedded multimedia. Its design allows to use it on several 
platforms, thanks to a plugin system allowing to choose the underlying 
graphical API. Pigment is the rendering engine of Elisa, the Fluendo 
Media Center project.

%package -n %libname-devel
Group: Development/C
Summary: Development headers for shared library of Pigment
Requires: %libname = %version
Provides: lib%name-devel = %version-%release

%description -n %libname-devel
Pigment is a Python library designed to easily build user interfaces 
with embedded multimedia. Its design allows to use it on several 
platforms, thanks to a plugin system allowing to choose the underlying 
graphical API. Pigment is the rendering engine of Elisa, the Fluendo 
Media Center project.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir %_libdir/%{name}-0.1
%dir %_libdir/%{name}-0.1/gstreamer
%_libdir/%{name}-0.1/*.so
%_libdir/%{name}-0.1/gstreamer/*.so
%py_puresitedir/pgm
%py_platsitedir/*.so

%files devel
%defattr(-,root,root)
%_libdir/%{name}-0.1/*.la
%_libdir/%{name}-0.1/gstreamer/*.la
%_includedir/*
%py_platsitedir/*.la

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root)
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%_libdir/pkgconfig/%{name}-render-0.1.pc
%_datadir/gtk-doc/html/pigment-render
