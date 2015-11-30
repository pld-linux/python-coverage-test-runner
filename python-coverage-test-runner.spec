#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define	module coverage-test-runner
Summary:	Python module for enforcing code coverage completeness
Name:		python-%{module}
Version:	1.10
Release:	3
License:	GPL v3+
Group:		Libraries/Python
Source0:	http://code.liw.fi/debian/pool/main/p/python-coverage-test-runner/%{name}_%{version}.orig.tar.gz
# Source0-md5:	dda01699195334d151b621800eaaf064
URL:		http://liw.fi/coverage-test-runner/
BuildRequires:	python-coverage
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-coverage
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CoverageTestRunner is a Python module for running unit tests and
failing them if the unit test module does not exercise all statements
in the module it tests.

For example, unit tests in module foo_tests.py are supposed to test
everything in the foo.py module, and if they don't, it's a bug in the
test coverage. It does not matter if other tests happen to test the
missing parts. The unit tests for the module should test everything in
that module.

%prep
%setup -q -n CoverageTestRunner-%{version}

%build
%py_build

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%{py_sitescriptdir}/CoverageTestRunner.py[co]
%{py_sitescriptdir}/CoverageTestRunner-%{version}-py*.egg-info
