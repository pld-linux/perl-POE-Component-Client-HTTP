#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Component-Client-HTTP
Summary:	POE::Component::Client::HTTP - a HTTP user-agent component
#Summary(pl):	
Name:		perl-POE-Component-Client-HTTP
Version:	0.55
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ae0189e86e72333dd52aa645e57c7510
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl-POE >= 0.11_06
BuildRequires:	perl-URI >= 1.11
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
POE::Component::Client::HTTP is an HTTP user-agent for POE.  It lets
other sessions run while HTTP transactions are being processed, and it
lets several HTTP transactions be processed in parallel.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"POE::Component::Client::HTTP")' \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

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
