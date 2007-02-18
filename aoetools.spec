Summary:	AoE tools - programs for users of ATA over Ethernet
Summary(pl.UTF-8):	Narzędzia AoE - programy dla używających ATA over Ethernet
Name:		aoetools
Version:	14
Release:	0.1
License:	GPL v2
Group:		Base/Utilities
Source0:	http://dl.sourceforge.net/aoetools/%{name}-%{version}.tar.gz
# Source0-md5:	592f9f031796b4f0b90166a8cd5f9e30
URL:		http://aoetools.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aoetools are programs for users of the ATA over Ethernet (AoE)
network storage protocol, a simple protocol for using storage over an
ethernet LAN. The vblade program (storage target) exports a block
device using AoE.

%description -l pl.UTF-8
aoetools to programy dla używających protokołu sieciowego składowania
danych ATA over Ethernet (AoE) - prostego protokołu do przechowywania
danych za pośrednictwem lokalnej sieci ethernetowej. Program vblade
(obiekt składowania) eksportuje urządzenie blokowe przy użyciu AoE.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README TODO
%attr(755,root,root) %{_sbindir}/aoe-discover
%attr(755,root,root) %{_sbindir}/aoe-flush
%attr(755,root,root) %{_sbindir}/aoe-interfaces
%attr(755,root,root) %{_sbindir}/aoe-stat
%attr(755,root,root) %{_sbindir}/aoe-mkdevs
%attr(755,root,root) %{_sbindir}/aoe-mkshelf
%attr(755,root,root) %{_sbindir}/aoe-revalidate
%attr(755,root,root) %{_sbindir}/aoeping
%{_mandir}/man8/aoe-discover.8*
%{_mandir}/man8/aoe-flush.8*
%{_mandir}/man8/aoe-interfaces.8*
%{_mandir}/man8/aoe-stat.8*
%{_mandir}/man8/aoe-mkdevs.8*
%{_mandir}/man8/aoe-mkshelf.8*
%{_mandir}/man8/aoe-revalidate.8*
%{_mandir}/man8/aoeping.8*
