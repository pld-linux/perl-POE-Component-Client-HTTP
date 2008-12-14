#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires network access)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Client-HTTP
Summary:	POE::Component::Client::HTTP - a HTTP user-agent component
Summary(pl.UTF-8):	POE::Component::Client::HTTP - komponent klienta HTTP
Name:		perl-POE-Component-Client-HTTP
Version:	0.87
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/POE/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2df38a1e86c4827dd5edc0867a263e0c
URL:		http://search.cpan.org/dist/POE-Component-Client-HTTP/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 1:0.3202
BuildRequires:	perl-URI >= 1.24
BuildRequires:	perl-libwww
%endif
Requires:	perl-POE >= 1:0.3202
Requires:	perl-POE-Component-Client-Keepalive
Requires:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Client::HTTP is an HTTP user-agent for POE.  It lets
other sessions run while HTTP transactions are being processed, and it
lets several HTTP transactions be processed in parallel.

%description -l pl.UTF-8
POE::Component::Client::HTTP to klient HTTP dla POE. Pozwala na
działanie innych sesji podczas wykonywania transakcji HTTP, a także
pozwala na równoległe wykonywanie kilku transakcji HTTP.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"POE::Component::Client::HTTP")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES* README
%{perl_vendorlib}/POE/Filter/HTTP*.pm
%{perl_vendorlib}/POE/Component/Client/HTTP.pm
%dir %{perl_vendorlib}/POE/Component/Client/HTTP
%{perl_vendorlib}/POE/Component/Client/HTTP/*.pm
%{_mandir}/man3/*
