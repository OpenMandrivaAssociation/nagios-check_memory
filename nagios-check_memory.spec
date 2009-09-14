%define name	nagios-check_memory
%define version	1.7
%define release	%mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Check memory
Group:		Networking/Other
License:	BSD
URL:		http://www.nagiosexchange.org/cgi-bin/page.cgi?g=Detailed%2F1789.html;d=1
Source0:	check_mem.pl.gz
Patch0:     check_memory-1.7-fix-warnings.patch
Patch1:     check_memory-1.7-dont-use-findbin.patch
Requires:   nagios-plugins
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
This plugin may be used as nrpe plugin and checks the amount of memory free,
used and total available by using the linux "free -mt" command. 

%prep
%setup -c -T
gunzip < %{SOURCE0} | gunzip > check_mem.pl
%patch0 -p 0
%patch1 -p 0
perl -pi -e 's|\@libdir@|%{_datadir}|' check_mem.pl

%build


%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_datadir}/nagios/plugins
install -m 755 check_mem.pl %{buildroot}%{_datadir}/nagios/plugins/check_memory

install -d -m 755 %{buildroot}%{_sysconfdir}/nagios/plugins.d
cat > %{buildroot}%{_sysconfdir}/nagios/plugins.d/check_memory.cfg <<'EOF'
define command{
	command_name	check_memory
	command_line	%{_datadir}/nagios/plugins/check_memory
}
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/nagios/plugins/check_memory
%config(noreplace) %{_sysconfdir}/nagios/plugins.d/check_memory.cfg
