%define base_name	icon-theme
%define theme_name	elementary

Name:			%{theme_name}-%{base_name}
Version:		2.7.1
Release:		%mkrel 1
Summary:		Elementary icons for GNOME Desktop
License:		GPLv2+
Group:			Graphical desktop/GNOME
Source:			http://launchpad.net/elementaryicons/2.0/%{version}/+download/%{name}-%{version}.tar.gz
URL:			https://launchpad.net/elementaryicons
BuildRequires: 		icon-naming-utils
Requires:		hicolor-icon-theme
Requires:		faenza-icon-theme
BuildArch:		noarch

%description
Elementary icons is an icon theme designed to be smooth,
sexy, clear, and efficient.

%prep
%setup -q -n %{name}/%{theme_name}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_iconsdir}/%{theme_name}
cp -Rf * %{buildroot}%{_iconsdir}/%{theme_name}/

%clean
rm -rf %{buildroot}

%post
%update_icon_cache %{_iconsdir}/%{theme_name}/

%postun
%clean_icon_cache %{_iconsdir}/%{theme_name}/

%files
%doc AUTHORS CONTRIBUTORS COPYING
%{_iconsdir}/%{theme_name}

