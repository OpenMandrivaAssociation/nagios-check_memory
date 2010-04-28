%define name    nagios-check_memory
%define version 1.0
%define release %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Epoch:      0
Summary:    Check memory
Group:      Networking/Other
License:    BSD
URL:        http://www.monitoringexchange.org/inventory/Check-Plugins/Operating-Systems/Linux/check_memory
Source0:    check_memory.pl
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This plugin may be used as nrpe plugin and checks the amount of memory free,
used and total available by using the linux "free -mt" command. 

%prep
%setup -c -T

%build


%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 %{SOURCE0} %{buildroot}%{_datadir}/nagios/plugins/check_memory.pl

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_memory.cfg <<'EOF'
define command{
    command_name    check_memory
    command_line    %{_datadir}/nagios/plugins/check_memory.pl
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/nagios/plugins/check_memory.pl
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_memory.cfg
