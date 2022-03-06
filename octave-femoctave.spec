%global oname FEMoctave
%global octpkg %(echo %{oname} | tr [:upper:] [:lower:])

#It requireas non-free software to work!

Summary:	A simple FEM package for solving boundary value problems in two space dimensions.
Name:		octave-%{octpkg}
Version:	2.0.3
Release:	1
Source0:	https://github.com/AndreasStahel/%{oname}/archive/v%{version}/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://github.com/AndreasStahel/%{oname}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 4.4.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A simple FEM package to use FEM for solving boundary value problems in
two space dimensions.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}

# remove backup files
#find . -name \*~ -delete

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

