Summary:	CloneCD image to ISO image file converter
Summary(pl.UTF-8):	Konwerter plików obrazów CloneCD do ISO
Name:		ccd2iso
Version:	0.3
Release:	3
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/ccd2iso/%{name}-%{version}.tar.gz
# Source0-md5:	a7df1c46cb710f2fc8ebd88c2e64ce65
URL:		http://sourceforge.net/projects/ccd2iso/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CloneCD image to ISO image file converter.

%description -l pl.UTF-8
Konwerter plików obrazów CloneCD do ISO.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
