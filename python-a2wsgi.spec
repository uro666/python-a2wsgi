%define module a2wsgi
%bcond_without test

Name:		python-a2wsgi
Version:	1.10.8
Release:	1
Summary:	Convert WSGI app to ASGI app or ASGI app to WSGI app
URL:		https://pypi.org/project/a2wsgi/
License:	Apache-2.0
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/a/a2wsgi/a2wsgi-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-asyncio)
BuildRequires:	python%{pyver}dist(httpx)
BuildRequires:	python%{pyver}dist(starlette)
BuildRequires:	python%{pyver}dist(pdm-backend)



%description
Convert WSGI app to ASGI app or ASGI app to WSGI app.

Pure Python. Only depend on the standard library.

Compared with other converters, the advantage is that a2wsgi will not
accumulate the requested content or response content in the memory,
so you don't have to worry about the memory limit caused by a2wsgi.

This problem exists in converters implemented by uvicorn/startlette
or hypercorn.

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py3_install

%if %{with test}
%check
# skip baize tests, not packaged
ignore='not test_baize_stream_response'
%{__python} -m pytest --import-mode append -v tests/ -k "$ignore"
%endif

%files
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}.dist-info
%license LICENSE
