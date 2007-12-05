%define name pigment
%define version 0.3.2
%define	fversion 0.3
%define svn 0
%if %svn
%define release %mkrel 0.%svn.1
%else
%define release %mkrel 1
%endif
%define major 1
%define libname %mklibname %name %major
%define develname %mklibname %name -d

Summary: Python user interface library with embedded multimedia
Name: %{name}
Version: %{version}
Release: %{release}
%if %svn
Source0: %{name}-%{svn}.tar.bz2
%else
Source0: http://elisa.fluendo.com/static/download/pigment/%{name}-%{version}.tar.bz2
%endif
License: LGPLv2+
Group: Development/Python
Url: https://core.fluendo.com/pigment/trac
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %svn
BuildRequires: autoconf
%endif
BuildRequires: libx11-devel
BuildRequires: libxrandr-devel
BuildRequires: gtk-doc
BuildRequires: libgstreamer0.10-devel
BuildRequires: libgstreamer0.10-plugins-base-devel
BuildRequires: gstreamer0.10-python
BuildRequires: glib2-devel
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

%package -n %develname
Group: Development/C
Summary: Development headers for shared library of Pigment
Requires: %libname = %version
Provides: %name-devel = %version-%release
Obsoletes: %{_lib}pigment0-devel

%description -n %develname
Pigment is a Python library designed to easily build user interfaces 
with embedded multimedia. Its design allows to use it on several 
platforms, thanks to a plugin system allowing to choose the underlying 
graphical API. Pigment is the rendering engine of Elisa, the Fluendo 
Media Center project.

%prep
%if %svn
%setup -q -n %name
%else
%setup -q
%endif

%build
%if %svn
./autogen.sh
%endif
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%dir %_libdir/%{name}-%{fversion}
%dir %_libdir/%{name}-%{fversion}/gstreamer
%_libdir/%{name}-%{fversion}/*.so
%_libdir/%{name}-%{fversion}/gstreamer/*.so
%py_puresitedir/pgm
%py_puresitedir/pypgmtools
%py_platsitedir/*.so
%dir %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gtk-doc/html/%{name}*

%files devel
%defattr(-,root,root)
%_libdir/%{name}-%{fversion}/*.la
%_libdir/%{name}-%{fversion}/gstreamer/*.la
%_includedir/*
%py_platsitedir/*.la

%files -n %libname
%defattr(-,root,root)
%_libdir/lib*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_libdir/lib*.so
%attr(644,root,root) %_libdir/lib*a
%_libdir/pkgconfig/%{name}-%{fversion}.pc

