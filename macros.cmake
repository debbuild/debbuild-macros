# SPDX-License-Identifier: MIT

#
# Macros for cmake
#
%_cmake_shared_libs -DBUILD_SHARED_LIBS:BOOL=ON
%_cmake_skip_rpath -DCMAKE_SKIP_RPATH:BOOL=ON
%__cmake /usr/bin/cmake

# - Set default compile flags
# - CMAKE_*_FLAGS_RELEASE are added *after* the *FLAGS environment variables
# and default to -O3 -DNDEBUG.  Strip the -O3 so we can override with *FLAGS
# - Turn on verbose makefiles so we can see and verify compile flags
# - Set default install prefixes and library install directories
# - Turn on shared libraries by default
%cmake \
  %{set_build_flags}; \
  %__cmake \\\
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
