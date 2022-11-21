# INSTRUCTIONS:
# extract your tarball, then:
# tar -xvf blender-3.3.1-linux-x64.tar.xz -C /path/to/
# ln -s /path/to/blender-3.3.1-linux-x64 ~/rpmbuild/BUILD/
#  (or just extract to ~/rpmbuild/BUILD/)
# rpmbuild -bb /path/to/blender.spec
# NOTE: the dirname under ~/rpmbuild/BUILD/ needs to be exactly blender-3.3.1-linux-x64
# (or you must change it in the install section

# RESULTS:
# -the rpm installs your new blender installation in /opt/blender-3.3.1-linux-x64/
# -and drops a symlink pointing to the blender executable in /usr/bin/blender-3.3.1
#   so you can just run $ blender-3.3.1
# -this installs a package called "blender_full", I'm not sure how to get it to install
#   without conflict if there's another blender installed

Name:          blender_full
# make sure there are no spaces in the version, as this will be used to create the path
Version:       3.3.1
Release:       buildbot
Summary:       A fully functional 3D modeling/rendering/animation package
License:       GPLv2+
Group:         Graphics/3D
Distribution:  Fedora Project
URL:           http://www.blender.org/

%define _blender_pkg_basename    blender-3.3.1-linux-x64
%define _blender_tarball         %{_blender_pkg_basename}.tar.xz
Source0:       https://builder.blender.org/download/daily/archive/%{_blender_tarball}
#Source0:       https://builder.blender.org/download/daily/archive/blender-3.3.1-stable+v33.b292cfe5a936-linux.x86_64-release.tar.xz
# Source0:      http://download.blender.org/source/%{name}-%{version}.tar.gz

Vendor:        Blender
Packager:      Blender builder - spec by insaner (insaner.com)
BuildArch:     x86_64

%define _arch_ext    _64


# otherwise, it will decide it is providing libGL.so.1  libGLU.so.1, which it technically isn't:
AutoReqProv: no

#Provides:      blender_%{version}
# NOTE:  the minimum glibc for blender-3.3; adjust as necessary:
#	 objdump -T /fittybones/tmp/blender_tmp/blender-3.3.1-linux-x64/blender | grep GLIBC | sed 's/.*GLIBC_\([.0-9]*\).*/\1/g' | sort -Vu | tail -1
#Requires:      libc.so.6(GLIBC_2.18)
Requires:      glibc >= 2.18

# otherwise, it will try to strip our binaries:
%global __os_install_post %{nil}

%define _blender_pkg_name       blender-%{version}
%define _blender_pkg_name_arch  %{_blender_pkg_name}%{_arch_ext}
%define _blender_install_dir    opt
%define _blender_install_path   /%{_blender_install_dir}/%{_blender_pkg_name}


%description
Blender is the in-house software of a high quality animation studio.
It has proven to be an extremely fast and versatile design instrument.
The software has a personal touch, offering a unique approach to the
world of three dimensions. Blender can be used to create TV
commercials, to make technical visualizations or business graphics, to
do some morphing, or to design user interfaces. Developers can easily
build and manage complex environments. The renderer is versatile and
extremely fast. All basic animation principles (curves and keys) are
implemented.

This is the self-contained buildbot release. This means it only 
(basically) depends on GLIBC 2.19, and that it will install in /opt
by default.


%files

%changelog
* Mon Nov 21 2022 insaner (insaner.com)
- modified for version 3.3
* Tue Jul 10 2018 insaner (insaner.com)
- modified for version 2.79b
* Fri Dec 9 2016 insaner (insaner.com)
- modified for version 2.78a
* Wed Feb 20 2016 insaner (insaner.com)
- first version of simple spec file


%install

rm -rf  %{_blender_install_dir}
mkdir -p  %{buildroot}%{_blender_install_path}
mkdir -p  %{buildroot}%{_bindir}
ln -s %{_blender_install_path}/blender %{buildroot}%{_bindir}/%{_blender_pkg_basename}
# echo HELLO %{_blender_install_path}=%{buildroot}=%{_bindir}=%{version}
# cp -a %{_builddir}/* %{buildroot}%{_blender_install_path}
#cp -a blender-2.79b-linux-glibc219-x86_64/* %{buildroot}%{_blender_install_path}
cp -a %{_blender_pkg_basename}/* %{buildroot}%{_blender_install_path}

%files 
/%{_blender_install_path}
/%{_bindir}/*


