%define	version 1.7
%define rel	1
%define	release	%mkrel %rel

Name:		safecopy
Summary:	A data recovery tool
Version:	%{version} 
Release:	%{release} 
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		https://safecopy.sourceforge.net
Group:		File tools
License:	GPLv2+

%description
safecopy is a data recovery tool which tries to extract as much data a
possible from a seekable but problematic (i.e., damaged sectors) source like
floppy drives, hard disk partitions, CDs, etc., where other tools like dd 
would fail due to I/O errors.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall

%files 
%doc README AUTHORS ChangeLog NEWS
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Sat Apr 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.7-1mdv2012.0
+ Revision: 794235
- version update 1.7

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6-2mdv2011.0
+ Revision: 614805
- the mass rebuild of 2010.1 packages

* Tue Nov 24 2009 Jérôme Brenier <incubusss@mandriva.org> 1.6-1mdv2010.1
+ Revision: 469702
- new version 1.6 (bugfix)

* Thu Oct 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1.5-1mdv2010.0
+ Revision: 452286
- update to new version 1.5

* Wed May 27 2009 Jérôme Brenier <incubusss@mandriva.org> 1.3-1mdv2010.0
+ Revision: 380070
- update to new version 1.3
- use makeinstall
- safecopy now has a man page
- fix license (GPLv2+)

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 0.2-2mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

