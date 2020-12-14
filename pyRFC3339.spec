#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyRFC3339
Version  : 1.1
Release  : 5
URL      : https://files.pythonhosted.org/packages/00/52/75ea0ae249ba885c9429e421b4f94bc154df68484847f1ac164287d978d7/pyRFC3339-1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/00/52/75ea0ae249ba885c9429e421b4f94bc154df68484847f1ac164287d978d7/pyRFC3339-1.1.tar.gz
Summary  : Generate and parse RFC 3339 timestamps
Group    : Development/Tools
License  : MIT
Requires: pyRFC3339-license = %{version}-%{release}
Requires: pyRFC3339-python = %{version}-%{release}
Requires: pyRFC3339-python3 = %{version}-%{release}
Requires: pytz
BuildRequires : buildreq-distutils3
BuildRequires : nose
BuildRequires : nose-python
BuildRequires : pytz

%description
===========

%package license
Summary: license components for the pyRFC3339 package.
Group: Default

%description license
license components for the pyRFC3339 package.


%package python
Summary: python components for the pyRFC3339 package.
Group: Default
Requires: pyRFC3339-python3 = %{version}-%{release}
Provides: pyrfc3339-python

%description python
python components for the pyRFC3339 package.


%package python3
Summary: python3 components for the pyRFC3339 package.
Group: Default
Requires: python3-core
Provides: pypi(pyrfc3339)
Requires: pypi(pytz)

%description python3
python3 components for the pyRFC3339 package.


%prep
%setup -q -n pyRFC3339-1.1
cd %{_builddir}/pyRFC3339-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583455749
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pyRFC3339
cp %{_builddir}/pyRFC3339-1.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/pyRFC3339/0f520aeab068326b612fea07b872cfd159bf22fa
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pyRFC3339/0f520aeab068326b612fea07b872cfd159bf22fa

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
