Summary:	AoE tools - programs for users of ATA over Ethernet
Summary(pl.UTF-8):	Narzędzia AoE - programy dla używających ATA over Ethernet
Name:		aoetools
Version:	27
Release:	0.1
License:	GPL v2
Group:		Base/Utilities
Source0:	http://dl.sourceforge.net/aoetools/%{name}-%{version}.tar.gz
# Source0-md5:	bc74d19c32a1fc006b45ff870322bedf
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
%doc NEWS README devnodes.txt
%attr(755,root,root) %{_sbindir}/aoe-discover
%attr(755,root,root) %{_sbindir}/aoe-flush
%attr(755,root,root) %{_sbindir}/aoe-interfaces
%attr(755,root,root) %{_sbindir}/aoe-stat
%attr(755,root,root) %{_sbindir}/aoe-mkdevs
%attr(755,root,root) %{_sbindir}/aoe-mkshelf
%attr(755,root,root) %{_sbindir}/aoe-revalidate
%attr(755,root,root) %{_sbindir}/aoe-version
%attr(755,root,root) %{_sbindir}/aoecfg
%attr(755,root,root) %{_sbindir}/aoeping
%attr(755,root,root) %{_sbindir}/coraid-update
%{_mandir}/man8/aoe-discover.8*
%{_mandir}/man8/aoe-flush.8*
%{_mandir}/man8/aoe-interfaces.8*
%{_mandir}/man8/aoe-stat.8*
%{_mandir}/man8/aoe-mkdevs.8*
%{_mandir}/man8/aoe-mkshelf.8*
%{_mandir}/man8/aoe-revalidate.8*
%{_mandir}/man8/aoe-version.8*
%{_mandir}/man8/aoecfg.8*
%{_mandir}/man8/aoeping.8*
%{_mandir}/man8/coraid-update.8*
