Summary:	Clone of zwordz game
Summary(pl.UTF-8):	Klon gry zwordz
Name:		WordZ
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://www.nooskewl.com/stuff/downloads/%{name}-src-%{version}.zip
# Source0-md5:	7daf77559740a0a204e0a2b3c7ebcad6
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-Makefile.patch
URL:		http://www.nooskewl.com/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple crossword game.

%description -l pl.UTF-8
Prosta gra krzyżówkowa.

%prep
%setup -q -n Wordz-src
%patch0 -p1
%{__sed} -i 's@getenv("WORDZ_DATA")@"%{_datadir}/%{name}"@' wordz.cpp

%build
%{__make} linux \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcxxflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name},%{_desktopdir},%{_pixmapsdir}}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
cp wordz $RPM_BUILD_ROOT%{_bindir}
cp data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/wordz
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
