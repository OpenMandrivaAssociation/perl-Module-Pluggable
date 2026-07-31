%define upstream_name	 Module-Pluggable
%define debug_package %{nil}

Name:       perl-%{upstream_name}
Version:    6.4
Release:    1

Summary:    Simple plugins for Perl modules

License:    Artistic/GPL
Group:      Development/Perl
Url:        https://github.com/simonwistow/Module-Pluggable
Source0:    https://cpan.metacpan.org/authors/id/S/SI/SIMONW/Module-Pluggable-%{version}.tar.gz

BuildRequires:	make
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Spec) >= 3.0.0
BuildRequires: perl(Module::Build) >= 0.380.0
BuildRequires: perl(Test::More) >= 0.620.0
BuildRequires: perl-devel

%description
This Perl module provides a simple but, hopefully, extensible way of having
'plugins' for your module.

%prep
%setup -q -n Module-Pluggable-6.4

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes INSTALL META.json META.yml README
%{perl_vendorlib}/Module
%{perl_vendorlib}/Devel
%{_mandir}/*/*
