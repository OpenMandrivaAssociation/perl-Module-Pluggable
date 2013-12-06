%define modname	Module-Pluggable
%define modver	3.9

Summary:	Simple plugins for Perl modules
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	13
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Module/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This Perl module provides a simple but, hopefully, extensible way of having
'plugins' for your module.

%prep
%setup -qn %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorarch}/Module
%{perl_vendorarch}/Devel
%{_mandir}/man3/*

