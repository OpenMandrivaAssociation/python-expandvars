%define module expandvars

Name:		python-expandvars
Version:	1.1.2
Release:	1
Summary:	Expand system variables Unix style
URL:		https://pypi.org/project/expandvars/
License:	MIT License
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/e/expandvars/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)

%description
Expand system variables Unix style

%files
%{python3_sitelib}/%{module}.py
%{python3_sitelib}/__pycache__/expandvars*
%{python3_sitelib}/%{module}-%{version}.dist-info/
%license LICENSE
%doc README.md
