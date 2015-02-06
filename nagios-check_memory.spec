%define name    nagios-check_memory
%define version 1.0
%define release 4

Name:       %{name}
Version:    %{version}
Release:    %{release}
Epoch:      1
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
install -m 755 %{SOURCE0} %{buildroot}%{_datadir}/nagios/plugins/check_memory

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_memory.cfg <<'EOF'
define command{
    command_name    check_memory
    command_line    %{_datadir}/nagios/plugins/check_memory
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/nagios/plugins/check_memory
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_memory.cfg


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-3mdv2011.0
+ Revision: 612984
- the mass rebuild of 2010.1 packages

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - drop .pl suffix, for consistency

* Wed Apr 28 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.0-1mdv2010.1
+ Revision: 540009
- switch to actual check_memory plugin instead of check_mem

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Dec 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-3mdv2009.1
+ Revision: 314639
- now a netapp plugin

* Thu Jun 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-2mdv2009.0
+ Revision: 229280
- requires nagios plugins
  this is not a noarch package

* Wed Jun 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-1mdv2009.0
+ Revision: 228996
- import nagios-check_memory


* Wed Jun 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.7-1mdv2009.0
- first mdv package
