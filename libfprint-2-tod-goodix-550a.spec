Name:           libfprint-2-tod-goodix-550a
Version:        0.0.9
Release:        %autorelease
Summary:        Proprietary driver for the Goodix fingerprint reader 27c6:550a

License:        Custom
URL:            https://download.lenovo.com/pccbbs/mobiles/r1slg01w.zip
Source0:        https://github.com/talal/libfprint-2-tod-goodix-550a/archive/refs/tags/%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  git
Requires:       libfprint-tod

%description
Proprietary driver for the Goodix fingerprint reader 27c6:550a, from Lenovo E14 Gen 4 Ubuntu driver.

%prep
%autosetup -n %{name}-%{version}

%install
# Create target directories
install -pdm 755 %{buildroot}%{_libdir}/libfprint-2/tod-1/
install -pdm 755 %{buildroot}%{_udevrulesdir}

# Install driver
install -m 0644 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-tod-goodix-550a-%{version}.so %{buildroot}%{_libdir}/libfprint-2/tod-1/libfprint-tod-goodix-550a-%{version}.so

# Install udev rule
install -m 0644 lib/udev/rules.d/60-libfprint-2-tod1-goodix.rules %{buildroot}%{_udevrulesdir}/60-libfprint-2-tod1-goodix.rules

%files
%defattr(-,root,root,-)
%{_libdir}/libfprint-2/tod-1/libfprint-tod-goodix-550a-%{version}.so
%{_udevrulesdir}/60-libfprint-2-tod1-goodix.rules

%changelog
%autochangelog
