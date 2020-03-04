#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pyRFC3339
Version  : 1.1
Release  : 1
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
Description
===========

.. image:: https://travis-ci.org/kurtraschke/pyRFC3339.svg?branch=master
    :target: https://travis-ci.org/kurtraschke/pyRFC3339

pyRFC3339 parses and generates :RFC:`3339`-compliant timestamps using `Python <https://www.python.org/>`_ `datetime.datetime <https://docs.python.org/2/library/datetime.html#datetime-objects>`_ objects.

>>> from pyrfc3339 import generate, parse
>>> from datetime import datetime
>>> import pytz
>>> generate(datetime.utcnow().replace(tzinfo=pytz.utc)) #doctest:+ELLIPSIS
'...T...Z'
>>> parse('2009-01-01T10:01:02Z')
datetime.datetime(2009, 1, 1, 10, 1, 2, tzinfo=<UTC>)
>>> parse('2009-01-01T14:01:02-04:00')
datetime.datetime(2009, 1, 1, 14, 1, 2, tzinfo=<UTC-04:00>)

Installation
============

To install the latest version from `PyPI <https://pypi.python.org/pypi>`_:

``$ pip install pyRFC3339``

To install the latest development version:

``$ pip install https://github.com/kurtraschke/pyRFC3339/tarball/master#egg=pyRFC3339-dev``

To build the documentation with Sphinx:

#. ``$ pip install Sphinx``
#. ``$ python setup.py build_sphinx``

The documentation is also available online at:

``https://pythonhosted.org/pyRFC3339/``

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
Provides: pypi(pyRFC3339)
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
export SOURCE_DATE_EPOCH=1583293529
# -Werror is for werrorists
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
