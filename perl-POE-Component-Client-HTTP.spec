#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# require network access
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Component-Client-HTTP
Summary:	POE::Component::Client::HTTP - a HTTP user-agent component
Summary(pl):	POE::Component::Client::HTTP - komponent klienta HTTP
Name:		perl-POE-Component-Client-HTTP
Version:	0.65
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9a2f493854380fe1aac7d769a4f9a437
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-POE >= 0.11_06
BuildRequires:	perl-URI >= 1.11
BuildRequires:	perl-libwww
%endif
Requires:	perl-POE
Requires:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Client::HTTP is an HTTP user-agent for POE.  It lets
other sessions run while HTTP transactions are being processed, and it
lets several HTTP transactions be processed in parallel.

%description -l pl
POE::Component::Client::HTTP to klient HTTP dla POE. Pozwala na
dzia³anie innych sesji podczas wykonywania transakcji HTTP, a tak¿e
pozwala na równoleg³e wykonywanie kilku transakcji HTTP.

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
%{perl_vendorlib}/POE/Component/Client/*.pm
%{_mandir}/man3/*
