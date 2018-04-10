# Change Log

## [**Upcoming**](https://galaxy.ansible.com/cloudalchemy/prometheus)

**Merged pull requests:**

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