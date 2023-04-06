%global pypi_name visualpython
%global pypi_version 2.3.5

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Visual Python is a GUI-based Python code generator, developed on the Jupyter Notebook as an extension

License:        GPLv3
URL:            https://github.com/visualpython/visualpython
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
<img src" width"45%">[![PyPI version shields.io]( ![Python: 3.x]( [![License:
GPLv3]( [![Downloads]( [![Issues: ](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
<img src" width"45%">[![PyPI version shields.io]( ![Python: 3.x]( [![License:
GPLv3]( [![Downloads]( [![Issues: ](


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/visualpy
%{_bindir}/visualpy.bat
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Apr 04 2023 jasmin - 2.3.5-1
- Initial package.
