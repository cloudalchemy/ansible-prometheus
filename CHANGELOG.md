# Change Log

## [**Next release**](https://galaxy.ansible.com/cloudalchemy/prometheus)

**Merged pull requests:**

- Synchronize files from cloudalchemy/skeleton [\#227](https://github.com/cloudalchemy/ansible-prometheus/pull/227) ([cloudalchemybot](https://github.com/cloudalchemybot))
- add RHEL8 and debian buster support; remove testing on debian jessie [\#226](https://github.com/cloudalchemy/ansible-prometheus/pull/226) ([paulfantom](https://github.com/paulfantom))
- Some "false" were incorrectly substituted to "no" [\#225](https://github.com/cloudalchemy/ansible-prometheus/pull/225) ([wzyboy](https://github.com/wzyboy))
- Update minimum required ansible version [\#224](https://github.com/cloudalchemy/ansible-prometheus/pull/224) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Moving to python 3 and dropping support for python 2.x \(on deployer host\) [\#223](https://github.com/cloudalchemy/ansible-prometheus/pull/223) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [2.10.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-08-19)
**Implemented enhancements:**

- Support recording rules without alerts [\#192](https://github.com/cloudalchemy/ansible-prometheus/issues/192)

**Fixed bugs:**

- Prometheus failed to start on Ubuntu 18.04: LimitNOFILE: Operation not permitted [\#190](https://github.com/cloudalchemy/ansible-prometheus/issues/190)

**Merged pull requests:**

- New prometheus/prometheus upstream release! [\#221](https://github.com/cloudalchemy/ansible-prometheus/pull/221) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Synchronize files from cloudalchemy/skeleton [\#220](https://github.com/cloudalchemy/ansible-prometheus/pull/220) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Allow specifying recording rules without alerting configuration [\#212](https://github.com/cloudalchemy/ansible-prometheus/pull/212) ([paulfantom](https://github.com/paulfantom))

## [2.9.3](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-08-14)
**Merged pull requests:**

- New prometheus/prometheus upstream release! [\#219](https://github.com/cloudalchemy/ansible-prometheus/pull/219) ([cloudalchemybot](https://github.com/cloudalchemybot))
- New prometheus/prometheus upstream release! [\#217](https://github.com/cloudalchemy/ansible-prometheus/pull/217) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [2.9.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-07-11)
**Merged pull requests:**

- New prometheus/prometheus upstream release! [\#216](https://github.com/cloudalchemy/ansible-prometheus/pull/216) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [2.9.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-05-27)
**Closed issues:**

- prometheus\_alert\_rules\_files link is broken [\#207](https://github.com/cloudalchemy/ansible-prometheus/issues/207)

**Merged pull requests:**

- New prometheus/prometheus upstream release! [\#209](https://github.com/cloudalchemy/ansible-prometheus/pull/209) ([cloudalchemybot](https://github.com/cloudalchemybot))
- add watchdog and clock skew alerts [\#206](https://github.com/cloudalchemy/ansible-prometheus/pull/206) ([paulfantom](https://github.com/paulfantom))

## [2.9.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-05-04)
**Fixed bugs:**

- Default CriticalDiskSpace alert using wrong label? [\#201](https://github.com/cloudalchemy/ansible-prometheus/issues/201)

**Merged pull requests:**

- Synchronize files from cloudalchemy/skeleton [\#205](https://github.com/cloudalchemy/ansible-prometheus/pull/205) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Wait for network to be online [\#204](https://github.com/cloudalchemy/ansible-prometheus/pull/204) ([paulfantom](https://github.com/paulfantom))
- New prometheus/prometheus upstream release! [\#203](https://github.com/cloudalchemy/ansible-prometheus/pull/203) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Update label for CriticalDiskSpace alert expression. [\#202](https://github.com/cloudalchemy/ansible-prometheus/pull/202) ([mjbnz](https://github.com/mjbnz))
- New prometheus/prometheus upstream release! [\#200](https://github.com/cloudalchemy/ansible-prometheus/pull/200) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [2.8.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-03-30)
**Merged pull requests:**

- set go\_arch as a var instead of calculating it during task execution [\#198](https://github.com/cloudalchemy/ansible-prometheus/pull/198) ([paulfantom](https://github.com/paulfantom))
- New prometheus/prometheus upstream release! [\#197](https://github.com/cloudalchemy/ansible-prometheus/pull/197) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Synchronize files from cloudalchemy/skeleton. [\#196](https://github.com/cloudalchemy/ansible-prometheus/pull/196) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [2.8.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-03-23)
**Implemented enhancements:**

- Get more recognition! [\#131](https://github.com/cloudalchemy/ansible-prometheus/issues/131)

**Fixed bugs:**

- Get more recognition! [\#131](https://github.com/cloudalchemy/ansible-prometheus/issues/131)

**Closed issues:**

- can't create prometheus user again [\#185](https://github.com/cloudalchemy/ansible-prometheus/issues/185)
- Implement Uninstalls based on specific variables [\#181](https://github.com/cloudalchemy/ansible-prometheus/issues/181)
- Allow Multiple blackbox exporters [\#179](https://github.com/cloudalchemy/ansible-prometheus/issues/179)
- Install prometheus using docker [\#173](https://github.com/cloudalchemy/ansible-prometheus/issues/173)

**Merged pull requests:**

- New prometheus upstream release! [\#193](https://github.com/cloudalchemy/ansible-prometheus/pull/193) ([cloudalchemybot](https://github.com/cloudalchemybot))
- prometheus.service.j2: stop using tests as filters [\#191](https://github.com/cloudalchemy/ansible-prometheus/pull/191) ([JordanP](https://github.com/JordanP))
- Preflight checks refactor [\#189](https://github.com/cloudalchemy/ansible-prometheus/pull/189) ([paulfantom](https://github.com/paulfantom))
- do not remove '/opt/prometheus' [\#188](https://github.com/cloudalchemy/ansible-prometheus/pull/188) ([paulfantom](https://github.com/paulfantom))
- Parameterise custom static targets file paths [\#187](https://github.com/cloudalchemy/ansible-prometheus/pull/187) ([hamishforbes](https://github.com/hamishforbes))
- Make prometheus user owner of prometheus folders [\#174](https://github.com/cloudalchemy/ansible-prometheus/pull/174) ([curantes](https://github.com/curantes))

## [2.7.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-03-04)
**Merged pull requests:**

- New prometheus upstream release! [\#186](https://github.com/cloudalchemy/ansible-prometheus/pull/186) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Reworked prometheus\_alert\_rules\_files [\#183](https://github.com/cloudalchemy/ansible-prometheus/pull/183) ([eRadical](https://github.com/eRadical))
- Separate test scenarios and run "privileged" one only on master branch [\#175](https://github.com/cloudalchemy/ansible-prometheus/pull/175) ([paulfantom](https://github.com/paulfantom))

## [2.6.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-02-19)
**Merged pull requests:**

- Add support for retention by size [\#182](https://github.com/cloudalchemy/ansible-prometheus/pull/182) ([SuperQ](https://github.com/SuperQ))

## [2.5.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-01-31)
## [2.5.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-01-30)
**Closed issues:**

- Allow specifying source url for Prometheus archive [\#176](https://github.com/cloudalchemy/ansible-prometheus/issues/176)

**Merged pull requests:**

- New prometheus upstream release! [\#178](https://github.com/cloudalchemy/ansible-prometheus/pull/178) ([cloudalchemybot](https://github.com/cloudalchemybot))
- New prometheus upstream release! [\#172](https://github.com/cloudalchemy/ansible-prometheus/pull/172) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [2.5.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2019-01-13)
**Fixed bugs:**

- Default rules not working correctly [\#157](https://github.com/cloudalchemy/ansible-prometheus/issues/157)

**Closed issues:**

- Executable HTML files in consoles and console\_libraries in prometheus\_config\_dir [\#168](https://github.com/cloudalchemy/ansible-prometheus/issues/168)
- Wrong home directory for the prometheus user [\#166](https://github.com/cloudalchemy/ansible-prometheus/issues/166)
- Autostart fails [\#162](https://github.com/cloudalchemy/ansible-prometheus/issues/162)
- prometheus\_alert\_rules are not copied as expected [\#148](https://github.com/cloudalchemy/ansible-prometheus/issues/148)

**Merged pull requests:**

- Change permissions of console templates to 0644. [\#171](https://github.com/cloudalchemy/ansible-prometheus/pull/171) ([dreig](https://github.com/dreig))
- Reuse `prometheus\_db\_dir` as prometheus user home directory [\#170](https://github.com/cloudalchemy/ansible-prometheus/pull/170) ([paulfantom](https://github.com/paulfantom))
- New prometheus upstream release! [\#167](https://github.com/cloudalchemy/ansible-prometheus/pull/167) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Alert expression fix [\#161](https://github.com/cloudalchemy/ansible-prometheus/pull/161) ([sjal](https://github.com/sjal))
- Fix running Dry Mode and improved tag usage [\#160](https://github.com/cloudalchemy/ansible-prometheus/pull/160) ([krzyzakp](https://github.com/krzyzakp))
- New prometheus upstream release! [\#159](https://github.com/cloudalchemy/ansible-prometheus/pull/159) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [2.4.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-10-29)
**Closed issues:**

- When used on GCE with gce\_sd\_config discovery scrape config, the ProtectHome=Yes option prevents Prometheus to discover Google Cloud Instances [\#153](https://github.com/cloudalchemy/ansible-prometheus/issues/153)

**Merged pull requests:**

- Add clarification surrounding when the .rules file is copied & where it goes [\#156](https://github.com/cloudalchemy/ansible-prometheus/pull/156) ([wbh1](https://github.com/wbh1))
- Resolves \#153 prometheus homedir set to /tmp [\#155](https://github.com/cloudalchemy/ansible-prometheus/pull/155) ([michalklempa](https://github.com/michalklempa))
- Document alert relabeling in README.md [\#152](https://github.com/cloudalchemy/ansible-prometheus/pull/152) ([juliusv](https://github.com/juliusv))

## [2.4.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-10-07)
**Merged pull requests:**

- Add support for alert relabeling [\#151](https://github.com/cloudalchemy/ansible-prometheus/pull/151) ([juliusv](https://github.com/juliusv))

## [2.3.4](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-10-05)
**Merged pull requests:**

- New prometheus upstream release! [\#150](https://github.com/cloudalchemy/ansible-prometheus/pull/150) ([cloudalchemybot](https://github.com/cloudalchemybot))
- move to ansible 2.7 [\#149](https://github.com/cloudalchemy/ansible-prometheus/pull/149) ([paulfantom](https://github.com/paulfantom))
- Fixed adding ansible comment in templates [\#147](https://github.com/cloudalchemy/ansible-prometheus/pull/147) ([carpenterbees](https://github.com/carpenterbees))
- Updates to set systemd ulimit for files to infinity [\#146](https://github.com/cloudalchemy/ansible-prometheus/pull/146) ([jalev](https://github.com/jalev))
- New prometheus upstream release! [\#145](https://github.com/cloudalchemy/ansible-prometheus/pull/145) ([cloudalchemybot](https://github.com/cloudalchemybot))
- update prometheus release [\#143](https://github.com/cloudalchemy/ansible-prometheus/pull/143) ([paulfantom](https://github.com/paulfantom))
- fix test condition [\#141](https://github.com/cloudalchemy/ansible-prometheus/pull/141) ([paulfantom](https://github.com/paulfantom))
- New prometheus upstream release! [\#140](https://github.com/cloudalchemy/ansible-prometheus/pull/140) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [2.3.3](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-09-06)
**Merged pull requests:**

- Missing protocol causes wrong url generated [\#137](https://github.com/cloudalchemy/ansible-prometheus/pull/137) ([sparanoid](https://github.com/sparanoid))

## [2.3.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-08-12)
**Closed issues:**

- \[Question\] can't specify blackbox as target [\#134](https://github.com/cloudalchemy/ansible-prometheus/issues/134)
- failed parsing YAML File [\#129](https://github.com/cloudalchemy/ansible-prometheus/issues/129)

**Merged pull requests:**

- New prometheus upstream release! [\#136](https://github.com/cloudalchemy/ansible-prometheus/pull/136) ([cloudalchemybot](https://github.com/cloudalchemybot))
- fixed typo [\#133](https://github.com/cloudalchemy/ansible-prometheus/pull/133) ([shibumi](https://github.com/shibumi))

## [2.3.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-07-15)
**Merged pull requests:**

- Fix custom rule/target file copy [\#132](https://github.com/cloudalchemy/ansible-prometheus/pull/132) ([SuperQ](https://github.com/SuperQ))

## [2.3.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-07-01)
**Fixed bugs:**

- Adding prometheus\_config\_flags\_extra without value [\#127](https://github.com/cloudalchemy/ansible-prometheus/issues/127)

**Merged pull requests:**

- use tox, ansible 2.6, and allow using remote docker host [\#130](https://github.com/cloudalchemy/ansible-prometheus/pull/130) ([paulfantom](https://github.com/paulfantom))

## [2.2.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-06-27)
**Merged pull requests:**

- Allow empty value in config\_flags\_extra [\#128](https://github.com/cloudalchemy/ansible-prometheus/pull/128) ([Turgon37](https://github.com/Turgon37))
- Allow role being run in check mode [\#126](https://github.com/cloudalchemy/ansible-prometheus/pull/126) ([joelpet](https://github.com/joelpet))
- add 'tags' support [\#125](https://github.com/cloudalchemy/ansible-prometheus/pull/125) ([soloradish](https://github.com/soloradish))

## [2.2.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-06-09)
**Merged pull requests:**

- Prometheus 2.3.0 [\#124](https://github.com/cloudalchemy/ansible-prometheus/pull/124) ([paulfantom](https://github.com/paulfantom))
- fix prometheus\_targets default value. [\#123](https://github.com/cloudalchemy/ansible-prometheus/pull/123) ([soloradish](https://github.com/soloradish))

## [2.1.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-06-02)
**Merged pull requests:**

- Let prometheus rule\_files config always be written [\#122](https://github.com/cloudalchemy/ansible-prometheus/pull/122) ([noraab](https://github.com/noraab))
- specify file name for dest in get\_url call [\#121](https://github.com/cloudalchemy/ansible-prometheus/pull/121) ([sarphram](https://github.com/sarphram))

## [2.1.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-05-27)
**Fixed bugs:**

- fix architecture var parsing [\#119](https://github.com/cloudalchemy/ansible-prometheus/pull/119) ([paulfantom](https://github.com/paulfantom))

**Closed issues:**

- Rate limiter in GitHub API [\#115](https://github.com/cloudalchemy/ansible-prometheus/issues/115)

**Merged pull requests:**

- use cloudalchemybot when accessing github api [\#120](https://github.com/cloudalchemy/ansible-prometheus/pull/120) ([paulfantom](https://github.com/paulfantom))

## [2.1.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-05-25)
**Fixed bugs:**

- Error creating systemd template [\#116](https://github.com/cloudalchemy/ansible-prometheus/issues/116)

**Merged pull requests:**

- Deploy console templates [\#118](https://github.com/cloudalchemy/ansible-prometheus/pull/118) ([SuperQ](https://github.com/SuperQ))
- fix condition in systemd template [\#117](https://github.com/cloudalchemy/ansible-prometheus/pull/117) ([Morsicus](https://github.com/Morsicus))

## [2.0.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-05-17)
**Implemented enhancements:**

- Provide checksum validation [\#104](https://github.com/cloudalchemy/ansible-prometheus/issues/104)
- Move to molecule 2.x [\#93](https://github.com/cloudalchemy/ansible-prometheus/issues/93)
- Hardening systemd unit for additional security [\#110](https://github.com/cloudalchemy/ansible-prometheus/pull/110) ([paulfantom](https://github.com/paulfantom))

**Fixed bugs:**

- Role fails on RedHat if SELinux is disabled [\#111](https://github.com/cloudalchemy/ansible-prometheus/issues/111)
- Can't download release due to Github redirect the request [\#101](https://github.com/cloudalchemy/ansible-prometheus/issues/101)

**Closed issues:**

- Explain how `prometheus\_targets` and `prometheus\_scrape\_config` work [\#105](https://github.com/cloudalchemy/ansible-prometheus/issues/105)

**Merged pull requests:**

- take care of SELinux only when it is enabled [\#112](https://github.com/cloudalchemy/ansible-prometheus/pull/112) ([paulfantom](https://github.com/paulfantom))
- add checksum verification [\#109](https://github.com/cloudalchemy/ansible-prometheus/pull/109) ([paulfantom](https://github.com/paulfantom))
- move to molecule 2.x [\#108](https://github.com/cloudalchemy/ansible-prometheus/pull/108) ([paulfantom](https://github.com/paulfantom))
- Offer a better IRC Web clients to users [\#107](https://github.com/cloudalchemy/ansible-prometheus/pull/107) ([Porkepix](https://github.com/Porkepix))
- Explain how to use prometheus\_targets and prometheus\_scrape\_configs [\#114](https://github.com/cloudalchemy/ansible-prometheus/pull/114) ([paulfantom](https://github.com/paulfantom))
- Remove prometheus 1.8 support [\#113](https://github.com/cloudalchemy/ansible-prometheus/pull/113) ([paulfantom](https://github.com/paulfantom))

## [1.1.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-04-20)
**Merged pull requests:**

- Fix version\_compare warnings [\#106](https://github.com/cloudalchemy/ansible-prometheus/pull/106) ([Porkepix](https://github.com/Porkepix))
- Separate downloading and unpacking prometheus archive [\#102](https://github.com/cloudalchemy/ansible-prometheus/pull/102) ([paulfantom](https://github.com/paulfantom))

## [1.1.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-04-17)
**Implemented enhancements:**

- Allow specifying `latest` version [\#90](https://github.com/cloudalchemy/ansible-prometheus/issues/90)

**Merged pull requests:**

- fast-finish failed travis builds [\#100](https://github.com/cloudalchemy/ansible-prometheus/pull/100) ([paulfantom](https://github.com/paulfantom))
- Use inline template for simpler targets population task [\#99](https://github.com/cloudalchemy/ansible-prometheus/pull/99) ([paulfantom](https://github.com/paulfantom))

## [1.1.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-04-13)
**Merged pull requests:**

- allow `latest` as prometheus\_version [\#94](https://github.com/cloudalchemy/ansible-prometheus/pull/94) ([paulfantom](https://github.com/paulfantom))
- add header for auto.sh script [\#92](https://github.com/cloudalchemy/ansible-prometheus/pull/92) ([paulfantom](https://github.com/paulfantom))
- Add synchronization of changelog and GitHub releases [\#91](https://github.com/cloudalchemy/ansible-prometheus/pull/91) ([paulfantom](https://github.com/paulfantom))
- CI automation scripts outsourcing [\#89](https://github.com/cloudalchemy/ansible-prometheus/pull/89) ([paulfantom](https://github.com/paulfantom))

## [1.0.10](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-04-10)
**Merged pull requests:**

- use new filter schema [\#88](https://github.com/cloudalchemy/ansible-prometheus/pull/88) ([paulfantom](https://github.com/paulfantom))

## [1.0.9](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-04-07)
**Merged pull requests:**

- Quick fix to allow multi-arch environments support [\#87](https://github.com/cloudalchemy/ansible-prometheus/pull/87) ([paulfantom](https://github.com/paulfantom))

## [1.0.8](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-04-05)
**Merged pull requests:**

- Retry when connecting to external services [\#86](https://github.com/cloudalchemy/ansible-prometheus/pull/86) ([paulfantom](https://github.com/paulfantom))

## [1.0.7](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-04-03)
**Merged pull requests:**

- test parametrization [\#85](https://github.com/cloudalchemy/ansible-prometheus/pull/85) ([paulfantom](https://github.com/paulfantom))

## [1.0.6](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-03-26)
**Merged pull requests:**

- Ubuntu bionic \(18.04\) support [\#82](https://github.com/cloudalchemy/ansible-prometheus/pull/82) ([paulfantom](https://github.com/paulfantom))

## [1.0.5](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-03-24)
**Merged pull requests:**

- ansible 2.5 [\#84](https://github.com/cloudalchemy/ansible-prometheus/pull/84) ([paulfantom](https://github.com/paulfantom))

## [1.0.4](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-03-22)
**Merged pull requests:**

- Modify when-statement to not include jinja2 templating delimiters [\#83](https://github.com/cloudalchemy/ansible-prometheus/pull/83) ([swesterveld](https://github.com/swesterveld))

## [1.0.3](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-03-15)
## [1.0.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-03-15)
**Merged pull requests:**

- Describe jmespath installation to virtualenv [\#81](https://github.com/cloudalchemy/ansible-prometheus/pull/81) ([bngsudheer](https://github.com/bngsudheer))
- SELinux support [\#79](https://github.com/cloudalchemy/ansible-prometheus/pull/79) ([paulfantom](https://github.com/paulfantom))

## [1.0.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-03-09)
**Merged pull requests:**

- bump prometheus version to 2.2 [\#80](https://github.com/cloudalchemy/ansible-prometheus/pull/80) ([paulfantom](https://github.com/paulfantom))

## [1.0.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-02-25)
**Implemented enhancements:**

- Support remote read option [\#73](https://github.com/cloudalchemy/ansible-prometheus/issues/73)
- Run Prometheus server without alertmanager option [\#18](https://github.com/cloudalchemy/ansible-prometheus/issues/18)

**Fixed bugs:**

- Wrong directory permissions [\#74](https://github.com/cloudalchemy/ansible-prometheus/issues/74)
- metrics\_path for local Prometheus endpoint [\#19](https://github.com/cloudalchemy/ansible-prometheus/issues/19)
- Wrong indent [\#36](https://github.com/cloudalchemy/ansible-prometheus/pull/36) ([paulfantom](https://github.com/paulfantom))

**Closed issues:**

- Allow multiple targets templates files. [\#58](https://github.com/cloudalchemy/ansible-prometheus/issues/58)
- Outdated documentation [\#1](https://github.com/cloudalchemy/ansible-prometheus/issues/1)

**Merged pull requests:**

- Custom target and rule files [\#59](https://github.com/cloudalchemy/ansible-prometheus/pull/59) ([paulfantom](https://github.com/paulfantom))

## [0.12.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-02-14)
**Merged pull requests:**

- Fix typo [\#78](https://github.com/cloudalchemy/ansible-prometheus/pull/78) ([swesterveld](https://github.com/swesterveld))

## [0.12.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-02-14)
**Merged pull requests:**

- Make Prometheus daemon restart/reload with sudo privileges. [\#77](https://github.com/cloudalchemy/ansible-prometheus/pull/77) ([swesterveld](https://github.com/swesterveld))

## [0.12.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-02-11)
**Merged pull requests:**

- add remote\_read functionality [\#76](https://github.com/cloudalchemy/ansible-prometheus/pull/76) ([paulfantom](https://github.com/paulfantom))

## [0.11.4](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-02-10)
**Fixed bugs:**

- change file permissions and ditch prometheus\_root\_dir [\#75](https://github.com/cloudalchemy/ansible-prometheus/pull/75) ([paulfantom](https://github.com/paulfantom))

## [0.11.3](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-02-10)
**Merged pull requests:**

- specify which tasks should use superuser permissions [\#72](https://github.com/cloudalchemy/ansible-prometheus/pull/72) ([paulfantom](https://github.com/paulfantom))
- adapt prometheus binary placement to hier\(7\) [\#71](https://github.com/cloudalchemy/ansible-prometheus/pull/71) ([paulfantom](https://github.com/paulfantom))

## [0.11.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-02-07)
**Closed issues:**

- File copy globbing [\#57](https://github.com/cloudalchemy/ansible-prometheus/issues/57)

**Merged pull requests:**

- Enable check mode in ansible [\#70](https://github.com/cloudalchemy/ansible-prometheus/pull/70) ([paulfantom](https://github.com/paulfantom))

## [0.11.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-02-06)
## [0.11.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-02-03)
**Merged pull requests:**

- Add support for remote write [\#69](https://github.com/cloudalchemy/ansible-prometheus/pull/69) ([paulfantom](https://github.com/paulfantom))

## [0.10.6](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-02-03)
**Merged pull requests:**

- Update ansible versions in tests [\#68](https://github.com/cloudalchemy/ansible-prometheus/pull/68) ([paulfantom](https://github.com/paulfantom))

## [0.10.5](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-22)
**Merged pull requests:**

- Set global values to prometheus defaults [\#67](https://github.com/cloudalchemy/ansible-prometheus/pull/67) ([paulfantom](https://github.com/paulfantom))

## [0.10.4](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-20)
**Implemented enhancements:**

- Add default CriticalRAMLoad alert rules [\#63](https://github.com/cloudalchemy/ansible-prometheus/issues/63)

**Merged pull requests:**

- Prometheus 2.1 [\#66](https://github.com/cloudalchemy/ansible-prometheus/pull/66) ([paulfantom](https://github.com/paulfantom))

## [0.10.3](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-17)
**Merged pull requests:**

- added CriticalRAMLoad [\#65](https://github.com/cloudalchemy/ansible-prometheus/pull/65) ([rdemachkovych](https://github.com/rdemachkovych))

## [0.10.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-17)
**Merged pull requests:**

- a little bit of python3 support [\#64](https://github.com/cloudalchemy/ansible-prometheus/pull/64) ([aeber](https://github.com/aeber))

## [0.10.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-16)
**Closed issues:**

- More preflight checks? [\#16](https://github.com/cloudalchemy/ansible-prometheus/issues/16)

**Merged pull requests:**

- validate prometheus\_config\_flags\_extra [\#62](https://github.com/cloudalchemy/ansible-prometheus/pull/62) ([paulfantom](https://github.com/paulfantom))

## [0.10.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-15)
**Implemented enhancements:**

- Support more operating systems in CI pipeline and meta/main.yml [\#42](https://github.com/cloudalchemy/ansible-prometheus/issues/42)

**Merged pull requests:**

- \[ci skip\] author info [\#61](https://github.com/cloudalchemy/ansible-prometheus/pull/61) ([paulfantom](https://github.com/paulfantom))
-  multiple target files loaded with file\_sd [\#60](https://github.com/cloudalchemy/ansible-prometheus/pull/60) ([paulfantom](https://github.com/paulfantom))

## [0.9.4](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-13)
**Merged pull requests:**

- use custom docker images in CI pipeline [\#43](https://github.com/cloudalchemy/ansible-prometheus/pull/43) ([paulfantom](https://github.com/paulfantom))

## [0.9.3](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-11)
**Merged pull requests:**

- cleaner tests [\#55](https://github.com/cloudalchemy/ansible-prometheus/pull/55) ([paulfantom](https://github.com/paulfantom))

## [0.9.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-07)
**Closed issues:**

- Convert scrape\_configs to simple attribute tree [\#45](https://github.com/cloudalchemy/ansible-prometheus/issues/45)

**Merged pull requests:**

- added i386 arch [\#54](https://github.com/cloudalchemy/ansible-prometheus/pull/54) ([rdemachkovych](https://github.com/rdemachkovych))
- Update README.md [\#53](https://github.com/cloudalchemy/ansible-prometheus/pull/53) ([paulfantom](https://github.com/paulfantom))

## [0.9.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-03)
**Closed issues:**

- What version of molecule are the tests written for? [\#44](https://github.com/cloudalchemy/ansible-prometheus/issues/44)

**Merged pull requests:**

- Update generatetag.sh [\#52](https://github.com/cloudalchemy/ansible-prometheus/pull/52) ([paulfantom](https://github.com/paulfantom))
- Simplify scrape configs [\#50](https://github.com/cloudalchemy/ansible-prometheus/pull/50) ([SuperQ](https://github.com/SuperQ))

## [0.9.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-02)
**Merged pull requests:**

- Docs [\#51](https://github.com/cloudalchemy/ansible-prometheus/pull/51) ([paulfantom](https://github.com/paulfantom))

## [0.8.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2018-01-02)
**Merged pull requests:**

- Update generatetag.sh [\#49](https://github.com/cloudalchemy/ansible-prometheus/pull/49) ([paulfantom](https://github.com/paulfantom))
- support older raspberry pi [\#48](https://github.com/cloudalchemy/ansible-prometheus/pull/48) ([paulfantom](https://github.com/paulfantom))

## [0.7.14](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-31)
**Merged pull requests:**

- Add link to demo site [\#47](https://github.com/cloudalchemy/ansible-prometheus/pull/47) ([paulfantom](https://github.com/paulfantom))

## [0.7.13](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-30)
**Merged pull requests:**

- Clean scrape config [\#46](https://github.com/cloudalchemy/ansible-prometheus/pull/46) ([paulfantom](https://github.com/paulfantom))

## [0.7.12](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-27)
**Merged pull requests:**

- armv7l ansible arch translates to armv7 go arch [\#41](https://github.com/cloudalchemy/ansible-prometheus/pull/41) ([anisse](https://github.com/anisse))

## [0.7.11](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-27)
**Merged pull requests:**

- storage retention [\#40](https://github.com/cloudalchemy/ansible-prometheus/pull/40) ([paulfantom](https://github.com/paulfantom))
- change alert rules name; take rules from wildcard [\#38](https://github.com/cloudalchemy/ansible-prometheus/pull/38) ([paulfantom](https://github.com/paulfantom))

## [0.7.10](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-22)
**Merged pull requests:**

- Update README.md [\#39](https://github.com/cloudalchemy/ansible-prometheus/pull/39) ([paulfantom](https://github.com/paulfantom))

## [0.7.9](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-18)
**Implemented enhancements:**

- metrics\_path for local Prometheus endpoint [\#27](https://github.com/cloudalchemy/ansible-prometheus/issues/27)

**Merged pull requests:**

- Fix default port for alertmanager [\#37](https://github.com/cloudalchemy/ansible-prometheus/pull/37) ([paulfantom](https://github.com/paulfantom))
- do not copy alert rules when there are none [\#35](https://github.com/cloudalchemy/ansible-prometheus/pull/35) ([paulfantom](https://github.com/paulfantom))

## [0.7.8](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-17)
**Merged pull requests:**

- Issue27 [\#32](https://github.com/cloudalchemy/ansible-prometheus/pull/32) ([paulfantom](https://github.com/paulfantom))

## [0.7.7](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-17)
**Merged pull requests:**

- add disk usage alert and reboot alert [\#31](https://github.com/cloudalchemy/ansible-prometheus/pull/31) ([paulfantom](https://github.com/paulfantom))
- add comments; clear README [\#30](https://github.com/cloudalchemy/ansible-prometheus/pull/30) ([paulfantom](https://github.com/paulfantom))

## [0.7.6](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-17)
**Merged pull requests:**

- CI fix [\#29](https://github.com/cloudalchemy/ansible-prometheus/pull/29) ([paulfantom](https://github.com/paulfantom))

## [0.7.5](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-15)
**Merged pull requests:**

- leave empty prometheus\_web\_external\_url for default [\#28](https://github.com/cloudalchemy/ansible-prometheus/pull/28) ([rdemachkovych](https://github.com/rdemachkovych))

## [0.7.4](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-15)
**Merged pull requests:**

- metrics path [\#24](https://github.com/cloudalchemy/ansible-prometheus/pull/24) ([paulfantom](https://github.com/paulfantom))

## [0.7.3](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-15)
**Closed issues:**

- Use systemd for service control [\#25](https://github.com/cloudalchemy/ansible-prometheus/issues/25)

**Merged pull requests:**

- fully switch to systemd module [\#26](https://github.com/cloudalchemy/ansible-prometheus/pull/26) ([paulfantom](https://github.com/paulfantom))
- auto set go architecture [\#23](https://github.com/cloudalchemy/ansible-prometheus/pull/23) ([paulfantom](https://github.com/paulfantom))
- simplify setting custom configuration file [\#21](https://github.com/cloudalchemy/ansible-prometheus/pull/21) ([paulfantom](https://github.com/paulfantom))

## [0.7.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-08)
**Merged pull requests:**

- Add newline before \[Unit\] section in service file [\#20](https://github.com/cloudalchemy/ansible-prometheus/pull/20) ([ecksun](https://github.com/ecksun))

## [0.7.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-06)
**Closed issues:**

- Debian support [\#3](https://github.com/cloudalchemy/ansible-prometheus/issues/3)
- Better handling of alerting rules [\#2](https://github.com/cloudalchemy/ansible-prometheus/issues/2)

**Merged pull requests:**

- Update README.md [\#17](https://github.com/cloudalchemy/ansible-prometheus/pull/17) ([paulfantom](https://github.com/paulfantom))
- Typo [\#14](https://github.com/cloudalchemy/ansible-prometheus/pull/14) ([paulfantom](https://github.com/paulfantom))
- Stop pipeline on any error [\#13](https://github.com/cloudalchemy/ansible-prometheus/pull/13) ([paulfantom](https://github.com/paulfantom))

## [0.7.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-01)
**Merged pull requests:**

- Alert rules and debian support [\#11](https://github.com/cloudalchemy/ansible-prometheus/pull/11) ([paulfantom](https://github.com/paulfantom))

## [0.6.12](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-12-01)
**Merged pull requests:**

- Fix tagging [\#12](https://github.com/cloudalchemy/ansible-prometheus/pull/12) ([paulfantom](https://github.com/paulfantom))

## [0.6.11](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-30)
**Merged pull requests:**

- Prometheus job [\#10](https://github.com/cloudalchemy/ansible-prometheus/pull/10) ([rdemachkovych](https://github.com/rdemachkovych))

## [0.6.9](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-28)
**Closed issues:**

- Parallel CI build [\#4](https://github.com/cloudalchemy/ansible-prometheus/issues/4)

**Merged pull requests:**

- Update main.yml [\#9](https://github.com/cloudalchemy/ansible-prometheus/pull/9) ([paulfantom](https://github.com/paulfantom))
- prometheus\_external\_labels variable assignment dynamically [\#6](https://github.com/cloudalchemy/ansible-prometheus/pull/6) ([rdemachkovych](https://github.com/rdemachkovych))

## [0.6.7](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-28)
**Merged pull requests:**

- Update generatetag.sh [\#8](https://github.com/cloudalchemy/ansible-prometheus/pull/8) ([paulfantom](https://github.com/paulfantom))

## [0.6.5](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-28)
**Merged pull requests:**

- Update generatetag.sh [\#7](https://github.com/cloudalchemy/ansible-prometheus/pull/7) ([paulfantom](https://github.com/paulfantom))
- test different ansible versions [\#5](https://github.com/cloudalchemy/ansible-prometheus/pull/5) ([paulfantom](https://github.com/paulfantom))

## [0.6.4](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-23)
## [0.6.3](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-23)
## [0.6.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-22)
## [0.6.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-22)
## [0.6.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-22)
## [0.5.5](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-13)
## [0.5.4](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-13)
## [0.5.3](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-11-07)
## [0.5.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-10-22)
## [0.5.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-10-17)
## [0.5.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-10-16)
## [0.4.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-10-05)
## [0.4.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-09-27)
## [0.3.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-08-21)
## [0.3.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-08-21)
## [0.3.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-07-21)
## [0.2.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-07-21)
## [0.1.7](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-07-11)
## [0.1.6](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-07-11)
## [0.1.5](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-07-11)
## [0.1.4](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-07-10)
## [0.1.3](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-06-20)
## [0.1.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-06-14)
## [0.1.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-06-13)
## [0.1.0](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-06-06)
## [0.0.6](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-05-23)
## [0.0.5](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-05-23)
## [0.0.4](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-05-15)
## [0.0.3](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-05-09)
## [0.0.2](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-05-09)
## [0.0.1](https://galaxy.ansible.com/cloudalchemy/prometheus) (2017-04-27)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*