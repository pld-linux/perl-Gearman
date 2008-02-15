#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Gearman
Summary:	Gearman - distributed job system
#Summary(pl.UTF-8):	
Name:		perl-Gearman
Version:	1.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/B/BR/BRADFITZ/%{pdir}-%{version}.tar.gz
# Source0-md5:	97403520bed18e1a7316001742381b2c
URL:		http://search.cpan.org/dist/Gearman/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-String-CRC32
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gearman is a distributed job system composed from clients, workers and servers.
Clients send job to one or more servers, then jobs are distributed out to farm of
workers.

This package contain Clients and Workers modules.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES HACKING TODO
%dir %{perl_vendorlib}/Gearman
%{perl_vendorlib}/Gearman/*.pm
%dir %{perl_vendorlib}/Gearman/ResponseParser
%{perl_vendorlib}/Gearman/ResponseParser/*.pm
%{_mandir}/man3/*
