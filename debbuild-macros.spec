%{!?_debconfigdir: %global _debconfigdir %{_prefix}/lib/debbuild}
%{!?_debmacrodir: %global _debmacrodir %{_debconfigdir}/macros.d}

Name:           debbuild-macros
Version:        0.0.4
Release:        0%{?dist}
Summary:        Various macros for extending debbuild functionality

%if "%{_vendor}" == "debbuild"
Group:          devel
Packager:       debbuild developers <https://github.com/debbuild/debbuild>
License:        MIT and LGPL-2.1+ and Apache-2.0 and GPL-2.0+
%else
Group:          Development/Tools%{?suse_version:/Building}
License:        MIT and LGPLv2+ and ASL 2.0 and GPLv2+
%endif

URL:            https://github.com/debbuild/debbuild-macros
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Requires:       debbuild >= 19.11.0
%if (0%{?ubuntu} && 0%{?ubuntu} < 1604) || (0%{?debian} && 0%{?debian} < 8)
Requires:       realpath
%endif
# Provides debpkg macros
Provides:       debbuild-macros-debpkg
# Provides cmake macros
Provides:       debbuild-macros-cmake
Provides:       cmake-deb-macros
# Provides mga macros
Provides:       debbuild-macros-mga-mkrel
Provides:       debbuild-macros-mga-mklibname
Provides:       mga-deb-macros
# Provides python macros
Provides:       debbuild-macros-python
Provides:       debbuild-macros-python2
Provides:       debbuild-macros-python3
Provides:       python-deb-macros
Provides:       python2-deb-macros
Provides:       python3-deb-macros
# Provides perl macros
Provides:       debbuild-macros-perl
Provides:       perl-deb-macros
# Provides golang macros
Provides:       debbuild-macros-golang
Provides:       go-deb-macros
Provides:       golang-deb-macros
# Provides apache httpd macros
Provides:       debbuild-macros-apache2
Provides:       apache2-deb-macros
# Provides gpgverify macros
Provides:       debbuild-macros-gpgverify
# Provides vpath macros
Provides:       debbuild-macros-vpath
# Provides ninja macros
Provides:       debbuild-macros-ninja
Provides:       ninja-deb-macros
# Provides meson macros
Provides:       debbuild-macros-meson
Provides:       meson-deb-macros
# Provides AppArmor macros
Provides:       debbuild-macros-apparmor
Provides:       apparmor-deb-macros
# Provides firewalld macros
Provides:       debbuild-macros-firewalld
Provides:       firewalld-deb-macros

%if 0%{?debian} >= 8 || 0%{?ubuntu} >= 1504
# Provides systemd macros
Provides:       debbuild-macros-systemd
Provides:       systemd-deb-macros
%endif

BuildArch:      noarch

%description
This package contains a set of RPM macros for debbuild,
designed in such a manner that it is trivial to port RPM
packaging to build Debian packages that are mostly in-line
with Debian Policy.

%prep
%autosetup -p1


%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_debconfigdir}
cp -av gpgverify %{buildroot}%{_debconfigdir}
cp -av cmake/cmake-* %{buildroot}%{_debconfigdir}
cp -av sysusers.generate-pre.sh %{buildroot}%{_debconfigdir}
mkdir -p %{buildroot}%{_debmacrodir}
cp -av macros.* %{buildroot}%{_debmacrodir}

%if (0%{?debian} && 0%{?debian} < 8) || (0%{?ubuntu} && 0%{?ubuntu} < 1504)
rm -fv %{buildroot}%{_debconfigdir}/sysusers.generate-pre.sh
rm -fv %{buildroot}%{_debmacrodir}/macros.systemd
rm -fv %{buildroot}%{_debmacrodir}/macros.sysusers
%endif

%files
%doc README.md
%license LICENSE*
%{_debconfigdir}/*


%changelog
* Thu Sep 17 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.4-0
- New release

* Thu Jul 30 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.3-0
- New release

* Fri Jan 10 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.2-0
- New release

* Mon Nov 25 2019 Neal Gompa <ngompa13@gmail.com> - 0.0.1-0
- Initial release
