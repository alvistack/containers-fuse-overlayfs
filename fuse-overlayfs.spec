# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: fuse-overlayfs
Epoch: 100
Version: 1.8
Release: 1%{?dist}
Summary: Implementation of overlay+shiftfs in FUSE for rootless containers
License: GPL-3.0-or-later
URL: https://github.com/containers/fuse-overlayfs/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: fuse3-devel
Requires: fuse3

%description
This package provides an overlayfs FUSE implementation so that it can be
used since Linux 4.18 by unprivileged users in an user namespace.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
./autogen.sh
./configure --prefix=%{_usr} --libdir=%{_libdir}
%{__make}

%install
%{__make} DESTDIR=%{buildroot} install-binPROGRAMS

%files
%license COPYING
%{_bindir}/%{name}

%changelog
