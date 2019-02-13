Name:		osg-repo-scripts
Version:	1.3.1
Release:	1%{?dist}
Summary:	rpm repo update scripts for osg repo servers

Group:		System Environment/Tools
License:	ASL 2.0
URL:		https://github.com/opensciencegrid/mash-scripts
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

#BuildRequires:	
Requires:	mash
Requires:	repoview
# does not work with createrepo 0.9.9-26 from EPEL
Requires:	createrepo >= 0.9.9-24
Requires:	createrepo <  0.9.9-25
Conflicts:	createrepo >= 0.9.9-25

%description
%{summary}

%prep
%setup -q

#%build

%install
install -d $RPM_BUILD_ROOT%{_bindir}/
install -d $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/
install -d $RPM_BUILD_ROOT%{_sysconfdir}/mash/
install -d $RPM_BUILD_ROOT%{_sysconfdir}/osg-koji-tags/
install -d $RPM_BUILD_ROOT%{_usr}/local/mirror/
install -d $RPM_BUILD_ROOT%{_datadir}/repo/

install -m 0755 bin/new_mashfile.sh     $RPM_BUILD_ROOT%{_bindir}/
install -m 0755 bin/update_all_repos.sh $RPM_BUILD_ROOT%{_bindir}/
install -m 0755 bin/update_mashfiles.sh $RPM_BUILD_ROOT%{_bindir}/
install -m 0755 bin/update_mirror.py    $RPM_BUILD_ROOT%{_bindir}/
install -m 0755 bin/update_repo.sh      $RPM_BUILD_ROOT%{_bindir}/

install -m 0644 etc/cron.d/repo      $RPM_BUILD_ROOT%{_sysconfdir}/cron.d/
install -m 0644 etc/mash_koji_config $RPM_BUILD_ROOT%{_sysconfdir}/
install -m 0644 etc/osg-koji-tags/osg-tags.exclude \
                       $RPM_BUILD_ROOT%{_sysconfdir}/osg-koji-tags/
install -m 0644 etc/repo_mirror_hostname $RPM_BUILD_ROOT%{_sysconfdir}/

# populated by update_mashfiles.sh
touch $RPM_BUILD_ROOT%{_sysconfdir}/osg-koji-tags/osg-tags

install -m 0644 etc/mash/mash.conf       $RPM_BUILD_ROOT%{_datadir}/repo/
install -m 0644 etc/rsyncd.conf          $RPM_BUILD_ROOT%{_datadir}/repo/
install -m 0644 share/repo/mash.template $RPM_BUILD_ROOT%{_datadir}/repo/

%files
#%doc
%{_bindir}/new_mashfile.sh
%{_bindir}/update_all_repos.sh
%{_bindir}/update_mashfiles.sh
%{_bindir}/update_mirror.py
%{_bindir}/update_repo.sh
%{_datadir}/repo/mash.conf
%{_datadir}/repo/mash.template
%{_datadir}/repo/rsyncd.conf
%config(noreplace) %{_sysconfdir}/cron.d/repo
%config(noreplace) %{_sysconfdir}/mash_koji_config
%config(noreplace) %{_sysconfdir}/osg-koji-tags/osg-tags.exclude
%ghost             %{_sysconfdir}/osg-koji-tags/osg-tags
%config(noreplace) %{_sysconfdir}/repo_mirror_hostname
%dir               %{_usr}/local/mirror

%changelog
* Wed Feb 13 2019 Carl Edquist <edquist@cs.wisc.edu> - 1.3.1-1
- Add config file for mirror hostname (SOFTWARE-3465)

* Mon Feb 11 2019 Carl Edquist <edquist@cs.wisc.edu> - 1.3-1
- Add support for rolling release repos (SOFTWARE-3465)

* Tue May 29 2018 Edgar Fajardo <emfajard@ucsd.edu> - 1.2-1
- Remove CHTC from the mirrorlist

* Thu Apr 12 2018 Carl Edquist <edquist@cs.wisc.edu> - 1.1-1
- Replace grid.iu.edu with opensciencegrid.org (SOFTWARE-3208)

* Thu Mar 15 2018 Carl Edquist <edquist@cs.wisc.edu> - 1.0-3
- Initial rpm packaging (SOFTWARE-3139)

