%define name        hytrust_accesscontrols
%define version     %(grep HCS_VERSION buildrev.h | cut -f3 -d " " | sed -e "s/\\"//g")
%define release     %(cat buildrev)
%define packager    HYTRUST <htdc-devel@hytrust.com>
%define installdir  opt/htac

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Package to support HyTrust Linux Access Controls functionality.

Group:          Development/Libraries
License:        Proprietary
Source0:        %{name}-%{version}.%{release}.tar.gz

Requires:       python(abi) = 2.7, sshpass, selinux-policy-devel, setools-console, python-requests
BuildArch:      noarch

%description
Linux Access Controls package for HyTrust DataControl.

%prep
%setup -c -q

%install
install -m 0755 -d $RPM_BUILD_ROOT/%{installdir}
install -m 0755 -d $RPM_BUILD_ROOT/%{installdir}/seaccess
install -m 0755 -d $RPM_BUILD_ROOT/%{installdir}/admin
install -m 0755 -d $RPM_BUILD_ROOT/%{installdir}/htmodules
install -m 0644 %{name}-%{version}/seaccess/__init__.py $RPM_BUILD_ROOT/%{installdir}/seaccess
install -m 0644 %{name}-%{version}/seaccess/core.py $RPM_BUILD_ROOT/%{installdir}/seaccess
install -m 0644 %{name}-%{version}/seaccess/config.py $RPM_BUILD_ROOT/%{installdir}/seaccess
install -m 0644 %{name}-%{version}/seaccess/htac.py $RPM_BUILD_ROOT/%{installdir}/seaccess
install -m 0644 %{name}-%{version}/seaccess/utils.py $RPM_BUILD_ROOT/%{installdir}/seaccess
install -m 0644 %{name}-%{version}/seaccess/operations.py $RPM_BUILD_ROOT/%{installdir}/seaccess
install -m 0644 %{name}-%{version}/seaccess/config_manager.py $RPM_BUILD_ROOT/%{installdir}/seaccess
install -m 0644 %{name}-%{version}/seaccess/htac_exceptions.py $RPM_BUILD_ROOT/%{installdir}/seaccess
install -m 0644 %{name}-%{version}/admin/__init__.py $RPM_BUILD_ROOT/%{installdir}/admin
install -m 0644 %{name}-%{version}/admin/htadmin.py $RPM_BUILD_ROOT/%{installdir}/admin
install -m 0644 %{name}-%{version}/admin/user_management.py $RPM_BUILD_ROOT/%{installdir}/admin
install -m 0644 %{name}-%{version}/admin/utils.py $RPM_BUILD_ROOT/%{installdir}/admin
install -m 0644 %{name}-%{version}/htpolicies/modules/htusers.pp $RPM_BUILD_ROOT/%{installdir}/htmodules
install -m 0644 %{name}-%{version}/htpolicies/modules/htaccesscontrol.pp $RPM_BUILD_ROOT/%{installdir}/htmodules

%files
/%{installdir}
%exclude /%{installdir}/seaccess/*.py
%exclude /%{installdir}/admin/*.py

%changelog
* %(date "+%a %b %d %Y") %packager  %{version}-%{release}
  - Initial HyTrust Access Controls release
