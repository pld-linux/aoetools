#
# TODO:
#		- add devices to static-dev
#		- vblade
#
Summary:	AoE tools - programs for users of ATA over Ethernet
Summary(pl):	Narzêdzia AoE - programy dla u¿ywaj±cych ATA over Ethernet
Name:		aoetools
Version:	5
Release:	0.1
License:	GPL v2
Group:		Base/Utilities
Source0:	http://dl.sourceforge.net/aoetools/%{name}-%{version}.tar.gz
# Source0-md5:	92412c457f2926c23ac6ca8f38b72fe8
URL:		http://aoetools.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aoetools are programs for users of the ATA over Ethernet (AoE)
network storage protocol, a simple protocol for using storage over an
ethernet LAN. The vblade program (storage target) exports a block
device using AoE.

%description -l pl
aoetools to programy dla u¿ywaj±cych protoko³u sieciowego sk³adowania
danych ATA over Ethernet (AoE) - prostego protoko³u do przechowywania
danych za po¶rednictwem lokalnej sieci ethernetowej. Program vblade
(obiekt sk³adowania) eksportuje urz±dzenie blokowe przy u¿yciu AoE.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_sbindir}/aoe-discover
%attr(755,root,root) %{_sbindir}/aoe-interfaces
%attr(755,root,root) %{_sbindir}/aoe-stat
%attr(755,root,root) %{_sbindir}/aoe-mkdevs
%attr(755,root,root) %{_sbindir}/aoe-mkshelf
%attr(755,root,root) %{_sbindir}/aoeping
%{_mandir}/man8/aoe-discover.8*
%{_mandir}/man8/aoe-interfaces.8*
%{_mandir}/man8/aoe-stat.8*
%{_mandir}/man8/aoe-mkdevs.8*
%{_mandir}/man8/aoe-mkshelf.8*
%{_mandir}/man8/aoeping.8*
