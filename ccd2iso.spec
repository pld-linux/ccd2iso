Summary:	CloneCD image to ISO image file converter
Name:		ccd2iso
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://dl.sourceforge.net/%{name}/%{name}.tar.gz
# Source0-md5:	2a478f2309608593035f1a095a616bd5
URL:		http://sourceforge.net/projects/ccd2iso/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CloneCD image to ISO image file converter.

%prep
%setup -q -n %{name}

%build
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
