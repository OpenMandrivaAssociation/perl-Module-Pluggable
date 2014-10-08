%define upstream_name	 Module-Pluggable
%define upstream_version 5.1

%define debug_package %{nil}

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    Simple plugins for Perl modules

License:    Artistic/GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec) >= 3.0.0
BuildRequires: perl(Module::Build) >= 0.380.0
BuildRequires: perl(Test::More) >= 0.620.0
BuildRequires: perl-devel

%description
This Perl module provides a simple but, hopefully, extensible way of having
'plugins' for your module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes INSTALL META.json META.yml MYMETA.yml README
%{perl_vendorlib}/Module
%{perl_vendorlib}/Devel
%{_mandir}/*/*

