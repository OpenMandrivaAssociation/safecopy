%define	version 1.3
%define rel	1
%define	release	%mkrel %rel

Name:		safecopy
Summary:	A data recovery tool
Version:	%{version} 
Release:	%{release} 
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://safecopy.sourceforge.net
Group:		File tools
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
rm -rf %{buildroot}
%makeinstall

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%{_bindir}/*
%{_mandir}/man1/*

