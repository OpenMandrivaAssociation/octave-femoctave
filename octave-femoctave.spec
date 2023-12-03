%global octpkg femoctave

#NOTE: some features will not work because require non-free software!

Summary:	A simple FEM package for solving boundary value problems in two space dimensions.
Name:		octave-femoctave
Version:	2.1.4
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
#Url:		https://packages.octave.org/femoctave/
Url:		https://github.com/AndreasStahel/FEMoctave/
Source0:	https://github.com/AndreasStahel/FEMoctave/archive/v.%{version}/femoctave-%{version}.tar.gz
#Source0:	https://github.com/AndreasStahel/FEMoctave/archive/refs/tags/v%{version}/femoctave-%{version}.tar.gz
#Source0:	https://github.com/AndreasStahel/FEMoctave/archive/refs/tags/v%{version}/FEMoctave-%{version}.tar.gz

BuildRequires:  octave-devel >= 5.2.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A simple FEM package to use FEM for solving boundary value problems in
two space dimensions.

NOTE: some features will not work because require non-free software.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n FEMoctave-v.%{version}

%build
%set_build_flags
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

