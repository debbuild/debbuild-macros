%global _debbuild_macrosdir %{_prefix}/lib/debbuild/macros.d

Name:           debbuild-macros
Version:        1
Release:        1%{?dist}
Summary:        Various macros for extending debbuild functionality

License:        CC0
URL:            https://gitlab.com/Conan_Kudo/debbuild-macros
Source0:        debbuild-macros.tar.gz

Requires:       debbuild
# Provides debpkg macros
Provides:       debbuild-macros-debpkg

%if 0%{?debian} >= 8 || 0%{?ubuntu} >= 1504
# Provides systemd macros
Provides:       debbuild-macros-systemd
%endif

%description
Various macros for debbuild

%prep
%setup -q -n %{name}


%build
# Nothing to build


%install
mkdir -p %{buildroot}%{_debbuild_macrosdir}
install -pm 0644 macros.debpkg %{buildroot}%{_debbuild_macrosdir}/macros.debpkg

%if 0%{?debian} >= 8 || 0%{?ubuntu} >= 1504
install -pm 0644 macros.systemd %{buildroot}%{_debbuild_macrosdir}/macros.systemd
%endif

%files
%{_debbuild_macrosdir}/macros.debpkg
%if 0%{?debian} >= 8 || %{?ubuntu} >= 1504
%{_debbuild_macrosdir}/macros.systemd
%endif



%changelog
* Wed Feb  3 2016 Neal Gompa <ngompa13@gmail.com> - 1-1
- Initial packaging
