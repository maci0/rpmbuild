Name:           dnscrypt
Version:        1.2.0
Release:        4%{?dist}
Summary:        Tool for securing communications between a client and a DNS resolver
Group:          Applications/Internet
License:        BSD
URL:            https://github.com/opendns/dnscrypt-proxy
Source0:        https://github.com/downloads/opendns/dnscrypt-proxy/%{name}-proxy-%{version}.tar.bz2
Source1:        dnscrypt.service
BuildRoot:      %{_tmppath}/%{name}-proxy-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  systemd

%description
dnscrypt-proxy provides local service which can be used directly as 
your local resolver or as a DNS forwarder, encrypting and authenticating
requests using the DNSCrypt protocol and passing them to an 
upstream server, by default OpenDNS who run this on their resolvers.

The DNSCrypt protocol uses high-speed high-security elliptic-curve 
cryptography and is very similar to DNSCurve, but focuses on securing 
communications between a client and its first-level resolver.

While not providing end-to-end security, it protects the local network, 
which is often the weakest point of the chain, against man-in-the-middle 
attacks. It also provides some confidentiality to DNS queries.


%prep
%setup -q -n %{name}-proxy-%{version}

%build
%configure --enable-plugins
make %{?_smp_mflags} CFLAGS="%{optflags} -fPIC" 

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_unitdir}
cp -r %{SOURCE1} %{buildroot}%{_unitdir}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING NEWS TECHNOTES THANKS
%{_bindir}/hostip
%{_sbindir}/%{name}-proxy
%{_unitdir}/%{name}.service
%{_mandir}/man8/hostip.8.gz
%{_mandir}/man8/%{name}-proxy.8.gz


%changelog
* Mon Jan 21 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-4
- build with --enable-plugins

* Mon Jan 05 2013 Marcel Wysocki <maci@satgnu.net> - 1.2.0-3
- remove pre/post scripts

* Sat Jan 05 2013 Marcel Wysocki <maci@satgnu.net> 1.2.0-2
- add systemd service file

* Tue Dec 18 2012 Marcel Wysocki <maci@satgnu.net> 1.2.0-1
- update to 1.2.0
- fedora port
- fixed dependencies
- fixed file section

* Sat Jan 28 2012 blino <blino> 0.8-1.mga2
+ Revision: 202564
- initial package release
- Created package structure for dnscrypt-proxy.

