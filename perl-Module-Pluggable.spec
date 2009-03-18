%define module	Module-Pluggable
%define name	perl-%{module}
%define version 3.9
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Simple plugins for Perl modules
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/Module/%{module}-%{version}.tar.gz
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This Perl module provides a simple but, hopefully, extensible way of having
'plugins' for your module.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorarch}/Module
%{perl_vendorarch}/Devel
%{_mandir}/*/*
