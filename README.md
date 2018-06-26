# debbuild-macros

This repository is a set of experimental RPM macros for [debbuild](https://github.com/ascherer/debbuild),
designed in such a manner that it's trivial to port RPM packaging to build Debian packages that are
mostly in-line with Debian Policy.

At this point, some of them somewhat work, and some don't work as intended.

# Licensing

Most of the macros are derived from Fedora or Mageia macros, which are licensed under the MIT License.

The systemd macros are derived from macros shipped with systemd, and thus are licensed under the
GNU Lesser General Public License, version 2.1 (or any later version, at your choice).
