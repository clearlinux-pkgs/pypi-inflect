#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-inflect
Version  : 5.6.2
Release  : 11
URL      : https://files.pythonhosted.org/packages/cb/db/cae5d8524c4b5e574c281895b212062f3b06d0e14186904ed71c538b4e90/inflect-5.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/cb/db/cae5d8524c4b5e574c281895b212062f3b06d0e14186904ed71c538b4e90/inflect-5.6.2.tar.gz
Summary  : Correctly generate plurals, singular nouns, ordinals, indefinite articles; convert numbers to words
Group    : Development/Tools
License  : MIT
Requires: pypi-inflect-license = %{version}-%{release}
Requires: pypi-inflect-python = %{version}-%{release}
Requires: pypi-inflect-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
.. image:: https://img.shields.io/pypi/v/inflect.svg
:target: `PyPI link`_
.. image:: https://img.shields.io/pypi/pyversions/inflect.svg
:target: `PyPI link`_

%package license
Summary: license components for the pypi-inflect package.
Group: Default

%description license
license components for the pypi-inflect package.


%package python
Summary: python components for the pypi-inflect package.
Group: Default
Requires: pypi-inflect-python3 = %{version}-%{release}

%description python
python components for the pypi-inflect package.


%package python3
Summary: python3 components for the pypi-inflect package.
Group: Default
Requires: python3-core
Provides: pypi(inflect)

%description python3
python3 components for the pypi-inflect package.


%prep
%setup -q -n inflect-5.6.2
cd %{_builddir}/inflect-5.6.2
pushd ..
cp -a inflect-5.6.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657924384
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-inflect
cp %{_builddir}/inflect-5.6.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-inflect/8e6689d37f82d5617b7f7f7232c94024d41066d1
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-inflect/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
