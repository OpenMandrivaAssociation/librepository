Name:           librepository
Version:        1.1.6
Release:        %mkrel 4
Summary:        Hierarchical repository abstraction layer
License:        LGPLv2+
Group:          System/Libraries
URL:            http://reporting.pentaho.org/
Source0:        http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
Patch0:         %{name}-1.1.2-fix-build.patch
BuildRequires:  ant, ant-contrib, ant-nodeps, java-devel, java-rpmbuild, jpackage-utils, libbase
Requires:       java, jpackage-utils, libbase
BuildArch:      noarch

%description
LibRepository provides a simple abstraction layer to access bulk content that
is organized in a hierarchical layer.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -c
%patch0 -p0
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib commons-logging-api libbase
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}
pushd $RPM_BUILD_ROOT%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
popd

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}


%changelog

* Sun Feb 10 2013 lmenut <lmenut> 1.1.6-4.mga3
+ Revision: 397720
- move java-rpmbuild in BuildRequires (mga #8270)

* Sat Jan 12 2013 umeabot <umeabot> 1.1.6-3.mga3
+ Revision: 358105
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sat Jan 21 2012 kamil <kamil> 1.1.6-2.mga2
+ Revision: 198941
- rebuild against new libbase-1.1.6

* Sat Jan 21 2012 kamil <kamil> 1.1.6-1.mga2
+ Revision: 198925
- change the javadoc subpackage group to Development/Java
- new version 1.1.6
- drop gcj support
- rediff and rename patch to fix-build

* Fri Mar 18 2011 dmorgan <dmorgan> 1.1.3-2.mga1
+ Revision: 74320
- Really build without gcj

* Wed Jan 26 2011 dmorgan <dmorgan> 1.1.3-1.mga1
+ Revision: 40160
- Adapt for mageia
- imported package librepository


* Thu Dec 02 2009 Caolan McNamara <caolanm@redhat.com> 1.1.3-1
- latest version

* Tue Nov 17 2009 Caolan McNamara <caolanm@redhat.com> 1.1.2-1
- latest version

* Fri Jul 24 2009 Caolan McNamara <caolanm@redhat.com> 1.0.0-2.OOo31
- make javadoc no-arch when building as arch-dependant aot

* Mon Mar 16 2009 Caolan McNamara <caolanm@redhat.com> 1.0.0-1.OOo31
- Post-release tuned for OpenOffice.org

* Mon Mar 09 2009 Caolan McNamara <caolanm@redhat.com> 0.2.0-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed May 07 2008 Caolan McNamara <caolanm@redhat.com> 0.1.6-1
- initial fedora import
