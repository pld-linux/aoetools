#
# TODO:
#		- add devices to static-dev
#		- vblade
#
Summary:	AoE tools - programs for users of ATA over Ethernet
Name:		aoetools
Version:	1
Release:	0.1
License:	GPL v2
Group:		Base/Utilities
Source0:	http://dl.sourceforge.net/aoetools/%{name}-%{version}.tar.gz
# Source0-md5:	e011ef5840d8ccc097d544ff0be33835
URL:		http://aoetools.sf.net/
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The aoetools are programs for users of the ATA over Ethernet (AoE)
network storage protocol, a simple protocol for using storage over an
ethernet LAN. The vblade program (storage target) exports a block
device using AoE.

%prep
%setup -q

%build

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
%{_mandir}/man?/aoe-discover*
%{_mandir}/man?/aoe-interfaces*
%{_mandir}/man?/aoe-stat*
%{_mandir}/man8/aoe-mkdevs*
%{_mandir}/man8/aoe-mkshelf*
