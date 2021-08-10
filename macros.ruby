# SPDX-License-Identifier: MIT

%__ruby %{_bindir}/ruby

%ruby_version %(%{__ruby} -r rbconfig -e 'print RbConfig::CONFIG["ruby_version"]')

%ruby_libprefixdir %(%{__ruby} -rrbconfig -e 'puts RbConfig::CONFIG["rubylibprefix"]')
%ruby_libdir %(%{__ruby} -rrbconfig -e 'puts RbConfig::CONFIG["rubylibdir"]')
%ruby_libarchdir %(%{__ruby} -rrbconfig -e 'puts RbConfig::CONFIG["archdir"]')

# This is the local lib/arch and should not be used for packaging.
%ruby_sitedir %(%{__ruby} -rrbconfig -e 'puts RbConfig::CONFIG["sitedir"]')
%ruby_sitelibdir %(%{__ruby} -rrbconfig -e 'puts RbConfig::CONFIG["sitelibdir"]')
%ruby_sitearchdir %(%{__ruby} -rrbconfig -e 'puts RbConfig::CONFIG["sitearchdir"]')

# This is the general location for libs/archs compatible with all
# or most of the Ruby versions available in the repositories.
%ruby_vendordir %(%{__ruby} -rrbconfig -e 'puts RbConfig::CONFIG["vendordir"]')
%ruby_vendorlibdir %(%{__ruby} -rrbconfig -e 'puts RbConfig::CONFIG["vendorlibdir"]')
%ruby_vendorarchdir %(%{__ruby} -rrbconfig -e 'puts RbConfig::CONFIG["vendorarchdir"]')
