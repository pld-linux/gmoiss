Summary:	Quantum Chemistry program
Summary(pl):	Program do chemii kwantowej
Name:		gmoiss
Version:	0.5
Release:	9
License:	GPL
Group:		X11/Applications/Science
Source0:	http://icm.linux.tucows.com/files/gnome/office/moiss-%{version}.tar.gz
# Source0-md5:	cf85ea01ac57afc56cc3cd6cbce5a82d
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-gsl.patch
Patch1:		%{name}-gcc33.patch
Patch2:		%{name}-am18.patch
URL:		http://moiss.pquim.unam.mx/moiss/
BuildRequires:	ORBit-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gsl-devel >= 0.9
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libPropList-devel
BuildRequires:	libtool
BuildRequires:	pvm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gmoiss is a program for Quantum Chemistry computations done with Monte
Carlo methods.

%description -l pl
Gmoiss jest programem do obliczeñ z dziedziny chemii kwantowej
metodami Monte Carlo.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f acinclude.m4 missing
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure \
	--enable-pvm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
