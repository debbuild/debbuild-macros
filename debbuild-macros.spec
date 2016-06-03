%global _debbuild_macrosdir %{_prefix}/lib/debbuild/macros.d

Name:           debbuild-macros
Version:        1
Release:        1%{?dist}
Summary:        Various macros for extending debbuild functionality

License:        CC0
URL:            https://gitlab.com/Conan_Kudo/debbuild-macros
Source0:        %{name}-%{version}.tar.gz

Requires:       debbuild
# Provides debpkg macros
Provides:       debbuild-macros-debpkg
# Provides cmake macros
Provides:       debbuild-macros-cmake
# Provides mga mkrel macros
Provides:       debbuild-macros-mga-mkrel
# Provides mga mklibname macros
Provides:       debbuild-macros-mga-mklibname

%if 0%{?debian} >= 8 || 0%{?ubuntu} >= 1504
# Provides systemd macros
Provides:       debbuild-macros-systemd
%endif

BuildArch:      noarch

%description
Various macros for debbuild

%prep
%setup -q


%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_debbuild_macrosdir}
install -pm 0644 macros.debpkg %{buildroot}%{_debbuild_macrosdir}/macros.debpkg
install -pm 0644 macros.cmake %{buildroot}%{_debbuild_macrosdir}/macros.cmake
install -pm 0644 macros.mga-mkrel %{buildroot}%{_debbuild_macrosdir}/macros.mga-mkrel
install -pm 0644 macros.mga-mklibname %{buildroot}%{_debbuild_macrosdir}/macros.mga-mklibname


%if 0%{?debian} >= 8 || 0%{?ubuntu} >= 1504
install -pm 0644 macros.systemd %{buildroot}%{_debbuild_macrosdir}/macros.systemd
%endif

%files
%defattr(-,root,root,-)
%{_debbuild_macrosdir}/macros.debpkg
%{_debbuild_macrosdir}/macros.cmake
%{_debbuild_macrosdir}/macros.mga-mkrel
%{_debbuild_macrosdir}/macros.mga-mklibname
%if 0%{?debian} >= 8 || %{?ubuntu} >= 1504
%{_debbuild_macrosdir}/macros.systemd
%endif



%changelog
* Wed Feb  3 2016 Neal Gompa <ngompa13@gmail.com> - 1-1
- Initial packaging
