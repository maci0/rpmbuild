%global _davsvn 2198
%ifarch i686
%global davarch x86
%endif
%ifarch x86_64
%global davarch x86_64
%endif

Name:               davmail
Version:            4.4.0
Release:            1%{?dist}
Summary:            POP/IMAP/SMTP/Caldav/Carddav/LDAP gateway for Microsoft Exchange
URL:                http://davmail.sourceforge.net/
License:            GPLv2+

Source0:            http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-srconly-%{version}-%{_davsvn}.tgz
Source1:            %{name}.desktop
Source2:            %{name}.ant.properties

Patch1:             0001-no-windows-service.patch
Patch2:             0002-no-osx-tray.patch
Patch3:             0003-base64-enc-dec.patch
Patch4:             0004-Set-classpath-add-target-davmail-lib.patch
Patch5:             0005-fix-launcher.patch

Requires:           java
Requires:           jpackage-utils
Requires:           jakarta-commons-httpclient
Requires:           jackrabbit-webdav
Requires:           log4j
Requires:           eclipse-swt


BuildRequires:      java-1.7.0-openjdk-devel
BuildRequires:      ant
BuildRequires:      desktop-file-utils
BuildRequires:      xml-commons-apis

BuildRequires:      jakarta-commons-httpclient
BuildRequires:      woodstox-core, stax2-api
BuildRequires:      jcifs, jackrabbit-webdav
# /usr/share/java/commons-logging.jar
BuildRequires:      htmlcleaner
# /usr/share/java/htmlcleaner/htmlcleaner.jar
BuildRequires:      slf4j
# /usr/share/java/slf4j/api.jar
BuildRequires:      eclipse-swt
# /usr/lib/java/swt.jar
BuildRequires:      tomcat-servlet-3.0-api
# /usr/share/java/tomcat-servlet-api.jar
BuildRequires:      javamail
# /usr/share/java/javamail/mail.jar
BuildRequires:      log4j
# /usr/share/java/log4j.jar


%description
DavMail is a POP/IMAP/SMTP/Caldav/Carddav/LDAP Exchange gateway allowing 
users to use any mail/calendar client with an Exchange server, even from 
the internet or behind a firewall through Outlook Web Access. DavMail 
now includes an LDAP gateway to Exchange global address book and user 
personal contacts to allow recipient address completion in mail compose 
window and full calendar support with attendees free/busy display.


%prep
%setup -q -n %{name}-%{version}-%{_davsvn}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p0

sed -i 's/\r//' releaseguide.txt releasenotes.txt



%build
ANT_OPTS="-Dfile.encoding=UTF-8" ant -propertyfile %{S:2} davmail-lib


%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
--dir $RPM_BUILD_ROOT%{_datadir}/applications \
%{S:1}

install -p -Dm644 src/java/tray2.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -p -Dm644 src/java/tray32.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -p -Dm644 src/java/tray48.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

install -p -Dm755 src/bin/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom
install -pm 644 dist/*.jar $RPM_BUILD_ROOT/%{_javadir}/%{name}.jar
%add_maven_depmap JPP-%{name}.pom %{name}.jar


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi


%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%doc releaseguide.txt releasenotes.txt
%{_javadir}/%{name}.jar
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mavendepmapfragdir}/%{name}
%{_mavenpomdir}/JPP-%{name}.pom

%changelog
* Tue Nov 26 2013 maci <maci@satgnu.net> - 4.4.0-1
- update to 4.4.0

* Mon Oct 14 2013 maci <maci@satgnu.net> - 4.3.4-2
- install into /usr/share/java
- add maven pom stuff
- minor cleanups

* Mon Oct 14 2013 maci <maci@satgnu.net> - 4.3.4-1
- update to 4.3.4

* Fri Jul 26 2013 maci <maci@satgnu.net> - 4.3.3-3
- fix some dependencies

* Thu Jun 27 2013 Marcin Dulak <Marcin.Dulak@gmail.com> 4.3.3-2
* bug #894413 c#21 : partly merge (no service or logging for now)

* Mon Jun 24 2013 Marcel Wysocki <maci@satgnu.net> - 4.3.3-1
- update to 4.3.3
- use srconly package

* Mon Jun 10 2013 Marcel Wysocki <maci@satgnu.net> - 4.3.2-1
- update to 4.3.2

* Thu Jun 06 2013 Marcel Wysocki <maci@satgnu.net> - 4.3.1-1
- update to 4.3.1

* Wed Jun 05 2013 Marcel Wysocki <maci@satgnu.net> - 4.3.0-2
- fix gmail typo in changelog
- regenerate icon cache

* Wed May 22 2013 Simone Sclavi <darkhado@gmail.com> 4.3.0-1
- Updated to 4.3.0 release
- Fixed 'class-path-in-manifest' rpmlint issue

* Fri Apr 26 2013 Marcel Wysocki <maci@satgnu.net> - 4.2.0-2
- removed OBS comment
- use install -p
- use global instead of define macro
- replaced davmail with name macro
- add missing requires

* Fri Mar 1 2013 Simone Sclavi <darkhado@gmail.com> 4.2.0-1
- Updated to 4.2.0 release

* Fri Feb 8 2013 Simone Sclavi <darkhado@gmail.com> 4.1.0-3
- Fixed summary
- Fixed dependencies for OBS building

* Fri Jan 11 2013 Marcel Wysocki <maci@satgnu.net> - 4.1.0-2
- add RPMGroup http://fedoraproject.org/wiki/RPMGroups

* Mon Dec 3 2012 Simone Sclavi <darkhado@gmail.com> 4.1.0-1
- Initial build 
