Summary:	Quantum Chemistry program
Summary(pl):	Program do chemii kwantowej
Name:		gmoiss
Version:	0.5
Release:	2
License:	GPL
Group:		X11/Applications/Science
Group(de):	X11/Applikationen/Wissenschaft
Group(pl):	X11/Aplikacje/Nauka
Source0:	http://icm.linux.tucows.com/files/gnome/office/moiss-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-gsl.patch
URL:		http://moiss.pquim.unam.mx/moiss/
BuildRequires:	ORBit-devel
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gsl-devel >= 0.9
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	libPropList-devel
BuildRequires:	libtool
BuildRequires:	pvm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gmoiss is a program for Quantum Chemistry computations done with Monte
Carlo methods.

%description -l pl
Gmoiss jest program do obliczeñ z dziedziny chemii kwantowej metodami
Monte Carlo.

%prep
%setup -q
%patch0 -p1

%build
rm -f acinclude.m4 missing
libtoolize --copy --force
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure \
	--enable-pvm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Scientific

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Scientific

#%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.lang
%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Scientific/*
