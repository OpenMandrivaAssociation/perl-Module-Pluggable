%define upstream_name	 Module-Pluggable
%define upstream_version 3.9

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 7

Summary:	Simple plugins for Perl modules
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This Perl module provides a simple but, hopefully, extensible way of having
'plugins' for your module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
