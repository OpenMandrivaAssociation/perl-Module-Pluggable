%define modname	Module-Pluggable
%define modver 5.1

Summary:	Simple plugins for Perl modules

Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Module/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires: perl(Module::Build::Compat)

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
# %{perl_vendorarch}/Module
# %{perl_vendorarch}/Devel
%{_mandir}/man3/*
%{perl_vendorlib}/Devel/InnerPackage.pm
%{perl_vendorlib}/Module/Pluggable.pm
%{perl_vendorlib}/Module/Pluggable/Object.pm


