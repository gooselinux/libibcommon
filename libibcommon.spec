Summary: OpenFabrics Alliance InfiniBand management common library
Name: libibcommon
Version: 1.2.0
Release: 3%{?dist}
License: GPLv2 or BSD
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source: http://www.openfabrics.org/downloads/management/%{name}-%{version}.tar.gz
Url: http://openfabrics.org/
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: libtool, automake, autoconf
ExcludeArch: s390 s390x

%description
libibcommon provides common utility functions for the OFA diagnostic and
management tools. 

%package devel
Summary: Development files for the libibcommon library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Development files for the libibcommon library.

%package static
Summary: Static library files for the libibcommon library
Group: System Environment/Libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
Static library files for the libibcommon library.

%prep
%setup -q
libtoolize --copy --force
touch NEWS README
autoreconf --install --force

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=${RPM_BUILD_ROOT} install
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libibcommon*.so.*
%doc AUTHORS COPYING ChangeLog 

%files devel
%defattr(-,root,root)
%{_libdir}/libibcommon.so
%dir %{_includedir}/infiniband
%{_includedir}/infiniband/*.h

%files static
%defattr(-,root,root)
%{_libdir}/libibcommon.a

%changelog
* Mon Jan 11 2010 Doug Ledford <dledford@redhat.com> - 1.2.0-3
- ExcludeArch on s390(x) as there is no hardware support there

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 22 2009 Doug Ledford <dledford@redhat.com> - 1.2.0-1
- Update to latest upstream version

* Tue Mar 03 2009 Robert Scheck <robert@fedoraproject.org> - 1.1.0-4
- Rebuilt against libtool 2.2

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 1.1.0-2
- Include /usr/include/infiniband directory.

* Sun Jun 08 2008 Doug Ledford <dledford@redhat.com> - 1.1.0-1
- Initial package for Fedora review process
