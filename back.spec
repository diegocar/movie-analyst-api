# cat /root/rpmbuild/SPECS/icecast.spec
Name:           movie-analyst-api
Version:        1.0.0
Release:        1
Summary:        A program that ejects movie backend for an app
Group:          
License:        GPL-2
URL:            https://github.com/diegocar/%{name}
Vendor:         PSL
Source:         %{name}-%{version}.tgz
Prefix:         %{_prefix}
Packager: 	Karthik
BuildRoot:      %{_tmppath}/%{name}-root

%description
Icecast is a streaming media server which currently supports Ogg Vorbis
and MP3 audio streams. It can be used to create an Internet radio
station or a privately running jukebox and many things in between.
It is very versatile in that new formats can be added relatively
easily and supports open standards for commuincation and interaction.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix} --mandir=%{_mandir} --sysconfdir=/etc

make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING NEWS TODO ChangeLog
%doc doc/*.html
%doc doc/*.jpg
%doc doc/*.css
%config(noreplace) /etc/%{name}.xml
%{_bindir}/icecast
%{_prefix}/share/icecast/*

%changelog

In this file, under % prep section you may noticed the macro “%setup -q -n %{name}-%{version}”. This macro executes the following command in the background.

cd /usr/src/redhat/BUILD
rm -rf icecast
gzip -dc /usr/src/redhat/SOURCES/icecast-2.3.3.tar.gz | tar -xvvf -
if [ $? -ne 0 ]; then
  exit $?
fi
cd icecast
cd /usr/src/redhat/BUILD/icecast
chown -R root.root .
chmod -R a+rX,g-w,o-w .