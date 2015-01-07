Name:           nethserver-mock
Version:        0.0.1
Release:        1%{?dist}
Summary:        RPM build automation scripts for NethServer packages
BuildArch:	noarch

License:        GPLv3
URL:            http://www.nethserver.org
Source0:        https://github.com/nethesis/nethserver-mock/%{version}/%{name}-%{version}.tar.gz

Requires: mock => 1.1.41
Requires: rpmdevtools >= 7.5
Requires: git >= 1.7.1
Requires: bash
Requires: coreutils
Requires: expect

%description
Provides build automation scripts for NethServer packages

%prep
%setup -q

%build


%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}/%{_bindir} %{buildroot}/%{_sysconfdir}/mock
install -vp src/bin/* %{buildroot}/%{_bindir}
install -vp src/mock/* %{buildroot}/%{_sysconfdir}/mock

%files
%defattr(-,root,root,-)
%{_bindir}/make-rpms
%{_bindir}/make-srpm
%{_bindir}/sign-rpms
%{_bindir}/prep-sources
%config(noreplace) %{_sysconfdir}/mock/nethserver-6.5-x86_64.cfg
%doc COPYING

%changelog
* Tue Dec 23 2014 Davide Principi <davide.principi@nethesis.it> - 0.0.1-1
- Initial version

