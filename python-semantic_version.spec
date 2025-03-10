# TODO: run tests using nose2 instead of nose (following upstream)
#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		semantic_version
Summary:	A library implementing the 'SemVer' scheme
Summary(pl.UTF-8):	Biblioteka implementująca schemat "SemVer"
Name:		python-%{module}
Version:	2.10.0
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/semantic-version/
Source0:	https://files.pythonhosted.org/packages/source/s/semantic-version/%{module}-%{version}.tar.gz
# Source0-md5:	e48abef93ba69abcd4eaf4640edfc38b
URL:		https://pypi.org/project/semantic-version/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with nose}
BuildRequires:	python-django >= 1.11
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with nose}
BuildRequires:	python3-django >= 2.2
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small Python library provides a few tools to handle SemVer in
Python. It follows strictly the 2.0.0 version of the SemVer scheme.

%description -l pl.UTF-8
Ta mała biblioteka Pythona dostarcza kilka narzędzi do obsługi SemVer
w Pythonie. Jest ściśle zgodna z wersją 2.0.0 schematu SemVer.

%package -n python3-%{module}
Summary:	A library implementing the 'SemVer' scheme
Summary(pl.UTF-8):	Biblioteka implementująca schemat "SemVer"
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
This small Python library provides a few tools to handle SemVer in
Python. It follows strictly the 2.0.0 version of the SemVer scheme.

%description -n python3-%{module} -l pl.UTF-8
Ta mała biblioteka Pythona dostarcza kilka narzędzi do obsługi SemVer
w Pythonie. Jest ściśle zgodna z wersją 2.0.0 schematu SemVer.

%package apidocs
Summary:	API documentation for Python semantic_version module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona semantic_version
Group:		Documentation

%description apidocs
API documentation for Python semantic_version module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona semantic_version.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(pwd) \
nosetests-%{py_ver} tests/test_*.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd) \
nosetests-%{py3_ver} tests/test_*.py
%endif
%endif

%if %{with doc}
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CREDITS ChangeLog LICENSE README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CREDITS ChangeLog LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_static,*.html,*.js}
%endif
