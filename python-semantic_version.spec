%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		semantic_version
Summary:	A library implementing the 'SemVer' scheme
Name:		python-%{module}
Version:	2.8.5
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/semantic-version/
Source0:	https://files.pythonhosted.org/packages/source/s/semantic-version/%{module}-%{version}.tar.gz
# Source0-md5:	76d7364def7ee487b6153d40b13de904
URL:		https://pypi.org/project/semantic-version/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This small python library provides a few tools to handle SemVer in
Python. It follows strictly the 2.0.0 version of the SemVer scheme.

%package -n python3-%{module}
Summary:	A library implementing the 'SemVer' scheme
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
This small python library provides a few tools to handle SemVer in
Python. It follows strictly the 2.0.0 version of the SemVer scheme.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
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
%doc CREDITS ChangeLog README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CREDITS ChangeLog README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
