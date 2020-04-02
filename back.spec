# cat /root/rpmbuild/SPECS/icecast.spec
Name:           movie-analyst-api
Version:        1.0.0
Release:        1%{?dist}
Summary:        A program that ejects movie backend for an app

Group:          
License:        GPL-2
URL:            https://github.com/diegocar/%{name}
Source:         %{name}-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-root

%description
Is the API, for movie's review web site, It shows the 
movie's review, with a score and the reviewer who do that

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