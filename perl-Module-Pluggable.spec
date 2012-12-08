%define upstream_name	 Module-Pluggable
%define upstream_version 3.9

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Simple plugins for Perl modules
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

BuildArch:	noarch

%description
This Perl module provides a simple but, hopefully, extensible way of having
'plugins' for your module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 3.900.0-7mdv2012.0
+ Revision: 765490
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 3.900.0-6
+ Revision: 763985
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 3.900.0-5
+ Revision: 667262
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 3.900.0-4mdv2011.0
+ Revision: 564541
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.900.0-3mdv2011.0
+ Revision: 555287
- rebuild

* Thu Aug 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.900.0-2mdv2010.1
+ Revision: 410594
- seems that module is arch-dependant?!

* Tue Aug 04 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 3.900.0-1mdv2010.0
+ Revision: 408864
- rebuild using %%perl_convert_version

* Wed Mar 18 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.9-1mdv2009.1
+ Revision: 357182
- new version

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 3.8-2mdv2009.0
+ Revision: 265418
- rebuild early 2009.0 package (before pixel changes)

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 3.8-1mdv2009.0
+ Revision: 193864
- update to new version 3.8

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 3.6-2mdv2008.1
+ Revision: 180481
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jul 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.6-1mdv2008.0
+ Revision: 48965
- update to new version 3.6


* Tue Mar 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 3.5-1mdv2007.0
+ Revision: 133696
- new version

* Tue Nov 28 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.4-1mdv2007.1
+ Revision: 87847
- new version

* Thu Nov 23 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.2-1mdv2007.1
+ Revision: 86555
- new version
- Import perl-Module-Pluggable

* Tue Jun 13 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.01-1mdv2007.0
- New release 3.01

* Wed Jun 07 2006 Guillaume Rousse <guillomovitch@mandriva.org> 3.0-1mdv2007.0
- New release 3.0
- spec cleanup

* Thu May 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 2.97-2mdk
- Fix According to perl Policy
	- Source URL

* Tue Feb 07 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.97-1mdk
- 2.97

* Thu Sep 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.96-1mdk
- New release 2.96

* Fri Aug 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.95-1mdk
- new release 
- fix sources url for rpmbuildupdate

* Sat Jul 16 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.9-1mdk
- 2.9

* Thu May 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.8-2mdk
- BuildRequires

* Thu May 05 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.8-1mdk
- First Mandriva release

