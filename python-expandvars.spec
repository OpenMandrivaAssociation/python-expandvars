%define module expandvars

Name:		python-expandvars
Version:	1.0.0
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


%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py3_install

%files
%{python3_sitelib}/%{module}.py
%{python3_sitelib}/__pycache__/expandvars*
%{python3_sitelib}/%{module}-%{version}.dist-info/
%license LICENSE
%doc README.md