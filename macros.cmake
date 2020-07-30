# SPDX-License-Identifier: MIT

#
# Macros for cmake
#
%_cmake_shared_libs -DBUILD_SHARED_LIBS:BOOL=ON
%_cmake_skip_rpath -DCMAKE_SKIP_RPATH:BOOL=ON
%__cmake /usr/bin/cmake
%__ctest /usr/bin/ctest
%__cmake_in_source_build 1
%__cmake_builddir %{!?__cmake_in_source_build:%{_vpath_builddir}}%{?__cmake_in_source_build:.}
%__cmake_configure %{_debconfigdir}/cmake-configure %{__cmake} "%{_vpath_srcdir}" "%{__cmake_builddir}"

# - Set default compile flags
# - CMAKE_*_FLAGS_RELEASE are added *after* the *FLAGS environment variables
# and default to -O3 -DNDEBUG.  Strip the -O3 so we can override with *FLAGS
# - Turn on verbose makefiles so we can see and verify compile flags
# - Set default install prefixes and library install directories
# - Turn on shared libraries by default
%cmake \
  %{set_build_flags}; \
  %{!?__cmake_in_source_build:%__cmake_configure}%{?__cmake_in_source_build:%__cmake} \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \\\
        -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \\\
        -DLIB_INSTALL_DIR:PATH=%{_libdir} \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        %{?_cmake_shared_libs}

%cmake_build \
  %{_debconfigdir}/cmake-build "%{__cmake_builddir}" %{?_smp_mflags}

%cmake_install \
  %{_debconfigdir}/cmake-install "%{__cmake_builddir}" "%{buildroot}"

%ctest \
  %{_debconfigdir}/cmake-test %{__ctest} "%{__cmake_builddir}" --output-on-failure --force-new-ctest-process %{?_smp_mflags}
