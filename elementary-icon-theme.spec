%define base_name	icon-theme
%define theme_name	elementary
%define version		2.4
%define name		%{theme_name}-%{base_name}
%define release		%mkrel 1

Name:			%{name}
Version:		%{version}
Release:		%{release}
Summary:		Elementary icons for GNOME Desktop
License:		GPLv2+
Group:			Graphical desktop/GNOME
Source:			http://launchpad.net/elementaryicons/2.0/%{version}/+download/%{theme_name}.tar.bz2
URL:			https://launchpad.net/elementaryicons
BuildRequires: 		icon-naming-utils
BuildArch: noarch

Requires:		hicolor-icon-theme

%ifarch i586
Requires:		libmurrine >= 0.91.0
%endif

%ifarch x86_64
Requires: lib64murrine >= 0.91.0
%endif

Requires: faenza-icon-theme
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Elementary icons is an icon theme designed to be smooth,
sexy, clear, and efficient.

%prep
rm -rf %buildroot
%setup -q -n %{theme_name}

%build

%install
%{__mkdir} -p %{buildroot}%{_iconsdir}/%{theme_name}
%{__cp} -Rf * %{buildroot}%{_iconsdir}/%{theme_name}/

%clean
rm -rf %buildroot

%post
%{update_icon_cache}
%postun
%{clean_icon_cache}

%files
%defattr(-,root,root)
%doc AUTHORS CONTRIBUTORS COPYING
%{_iconsdir}/%{theme_name}/*