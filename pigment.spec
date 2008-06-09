%define	fversion	0.3

%define svn	0
%define rel	2
%if %svn
%define release	%mkrel 0.%svn.%rel
%else
%define release	%mkrel %rel
%endif

%define major		4
%define libname		%mklibname %name %major
%define develname	%mklibname %name -d

Summary:	User interface library with embedded multimedia
Name:		pigment
Version:	0.3.5
Release:	%{release}
%if %svn
Source0:	%{name}-%{svn}.tar.lzma
%else
Source0:	http://elisa.fluendo.com/static/download/pigment/%{name}-%{version}.tar.gz
%endif
License:	LGPLv2+
Group:		Development/C
URL:		http://elisa.fluendo.com/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %svn
BuildRequires:	autoconf
%endif
BuildRequires:	libx11-devel
BuildRequires:	libxrandr-devel
BuildRequires:	gtk-doc
BuildRequires:	libgstreamer-devel >= 0.10
BuildRequires:	libgstreamer0.10-plugins-base-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	glib2-devel
BuildRequires:	cairo-devel
BuildRequires:	pango-devel
BuildRequires:	mesaglu-devel

%description
Pigment is a library designed to easily build user interfaces 
with embedded multimedia. Its design allows to use it on several 
platforms, thanks to a plugin system allowing to choose the underlying 
graphical API. Pigment is the rendering engine of Elisa, the Fluendo 
Media Center project.

%package devel
Group: Development/C
Summary: Development headers for Pigment
Requires: %{name}

%description devel
Pigment is a library designed to easily build user interfaces 
with embedded multimedia. Its design allows to use it on several 
platforms, thanks to a plugin system allowing to choose the underlying 
graphical API. Pigment is the rendering engine of Elisa, the Fluendo 
Media Center project.

%package -n %{libname}
Group: System/Libraries
Summary: Shared library of Pigment

%description -n %{libname}
Pigment is a library designed to easily build user interfaces 
with embedded multimedia. Its design allows to use it on several 
platforms, thanks to a plugin system allowing to choose the underlying 
graphical API. Pigment is the rendering engine of Elisa, the Fluendo 
Media Center project.

%package -n %{develname}
Group: Development/C
Summary: Development headers for shared library of Pigment
Requires: %{libname} = %version
Provides: lib%{name}-devel = %{version}-%{release}
Obsoletes: %{mklibname pigment 0 -d}

%description -n %{develname}
Pigment is a library designed to easily build user interfaces 
with embedded multimedia. Its design allows to use it on several 
platforms, thanks to a plugin system allowing to choose the underlying 
graphical API. Pigment is the rendering engine of Elisa, the Fluendo 
Media Center project.

%prep
%if %svn
%setup -q -n %{name}
%else
%setup -q
%endif

%build
%if %svn
./autogen.sh
%else
# (Anssi 03/2008) drop rpath on x86_64
autoreconf
%endif
%configure2_5x --enable-gtk-doc
make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%dir %{_libdir}/%{name}-%{fversion}/%{version}
%{_libdir}/%{name}-%{fversion}/%{version}/*.so
%dir %{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gtk-doc/html/%{name}*

%files devel
%defattr(-,root,root)
%{_libdir}/%{name}-%{fversion}/%{version}/*.*a
%{_includedir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib*.so
%attr(644,root,root) %{_libdir}/lib*a
%{_libdir}/pkgconfig/%{name}-gtk-%{fversion}.pc
%{_libdir}/pkgconfig/%{name}-%{fversion}.pc

