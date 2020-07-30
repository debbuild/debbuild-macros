%{!?_debconfigdir: %global _debconfigdir %{_prefix}/lib/debbuild}
%{!?_debmacrodir: %global _debmacrodir %{_debconfigdir}/macros.d}

Name:           debbuild-macros
Version:        0.0.2
Release:        0%{?dist}
Summary:        Various macros for extending debbuild functionality

%if %{_vendor} == "debbuild"
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
install -pm 0755 gpgverify %{buildroot}%{_debconfigdir}/gpgverify
install -pm 0755 cmake-configure %{buildroot}%{_debconfigdir}/cmake-configure
install -pm 0755 cmake-build %{buildroot}%{_debconfigdir}/cmake-build
install -pm 0755 cmake-install %{buildroot}%{_debconfigdir}/cmake-install
install -pm 0755 cmake-test %{buildroot}%{_debconfigdir}/cmake-test
mkdir -p %{buildroot}%{_debmacrodir}
install -pm 0644 macros.debpkg %{buildroot}%{_debmacrodir}/macros.debpkg
install -pm 0644 macros.cmake %{buildroot}%{_debmacrodir}/macros.cmake
install -pm 0644 macros.mga-mkrel %{buildroot}%{_debmacrodir}/macros.mga-mkrel
install -pm 0644 macros.mga-mklibname %{buildroot}%{_debmacrodir}/macros.mga-mklibname
install -pm 0644 macros.python %{buildroot}%{_debmacrodir}/macros.python
install -pm 0644 macros.python2 %{buildroot}%{_debmacrodir}/macros.python2
install -pm 0644 macros.python3 %{buildroot}%{_debmacrodir}/macros.python3
install -pm 0644 macros.perl %{buildroot}%{_debmacrodir}/macros.perl
install -pm 0644 macros.golang %{buildroot}%{_debmacrodir}/macros.golang
install -pm 0644 macros.apache2 %{buildroot}%{_debmacrodir}/macros.apache2
install -pm 0644 macros.gpgverify %{buildroot}%{_debmacrodir}/macros.gpgverify
install -pm 0644 macros.vpath %{buildroot}%{_debmacrodir}/macros.vpath
install -pm 0644 macros.ninja %{buildroot}%{_debmacrodir}/macros.ninja


%if 0%{?debian} >= 8 || 0%{?ubuntu} >= 1504
install -pm 0644 macros.systemd %{buildroot}%{_debmacrodir}/macros.systemd
%endif

%files
%doc README.md
%license LICENSE*
%{_debconfigdir}/gpgverify
%{_debconfigdir}/cmake-*
%{_debmacrodir}/macros.debpkg
%{_debmacrodir}/macros.cmake
%{_debmacrodir}/macros.mga-mkrel
%{_debmacrodir}/macros.mga-mklibname
%{_debmacrodir}/macros.python*
%{_debmacrodir}/macros.perl
%{_debmacrodir}/macros.golang
%{_debmacrodir}/macros.apache2
%{_debmacrodir}/macros.gpgverify
%{_debmacrodir}/macros.vpath
%{_debmacrodir}/macros.ninja
%if 0%{?debian} >= 8 || 0%{?ubuntu} >= 1504
%{_debmacrodir}/macros.systemd
%endif



%changelog
* Fri Jan 10 2020 Neal Gompa <ngompa13@gmail.com> - 0.0.2-0
- New release

* Mon Nov 25 2019 Neal Gompa <ngompa13@gmail.com> - 0.0.1-0
- Initial release
