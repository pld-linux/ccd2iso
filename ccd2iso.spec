Summary:	CloneCD image to ISO image file converter
Summary(pl):	Konwerter plików obrazów CloneCD do ISO
Name:		ccd2iso
Version:	0.1
Release:	2
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/ccd2iso/%{name}.tar.gz
# Source0-md5:	2a478f2309608593035f1a095a616bd5
URL:		http://sourceforge.net/projects/ccd2iso/
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CloneCD image to ISO image file converter.

%description -l pl
Konwerter plików obrazów CloneCD do ISO.

%prep
%setup -q -n %{name}

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
