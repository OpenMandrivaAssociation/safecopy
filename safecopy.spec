%define	version 0.2
%define rel	2
%define	release	%mkrel %rel

Name:		safecopy
Summary:	A data recovery tool
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://safecopy.sourceforge.net
Group:		File tools
License:	GPL

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
rm -rf $RPM_BUILD_ROOT
install -m755 src/safecopy -D $RPM_BUILD_ROOT%{_bindir}/safecopy

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%{_bindir}/*


