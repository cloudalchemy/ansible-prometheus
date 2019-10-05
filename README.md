<p><img src="https://cdn.worldvectorlogo.com/logos/prometheus.svg" alt="prometheus logo" title="prometheus" align="right" height="60" /></p>

# Ansible Role: prometheus

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-prometheus.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-prometheus)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.prometheus-blue.svg)](https://galaxy.ansible.com/cloudalchemy/prometheus/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-prometheus.svg)](https://github.com/cloudalchemy/ansible-prometheus/tags)
[![IRC](https://img.shields.io/badge/irc.freenode.net-%23cloudalchemy-yellow.svg)](https://kiwiirc.com/nextclient/#ircs://irc.freenode.net/#cloudalchemy)

## Description

Deploy [Prometheus](https://github.com/prometheus/prometheus) monitoring system using ansible.

### Upgradability notice

When upgrading from <= 2.4.0 version of this role to >= 2.4.1 please turn off your prometheus instance. More in [2.4.1 release notes](https://github.com/cloudalchemy/ansible-prometheus/releases/tag/2.4.1)

## Requirements

- Ansible >= 2.6 (It might work on previous versions, but we cannot guarantee it)
- jmespath on deployer machine. If you are using Ansible from a Python virtualenv, install *jmespath* to the same virtualenv via pip.
- gnu-tar on Mac deployer host (`brew install gnu-tar`)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `prometheus_version` | 2.13.0 | Prometheus package version. Also accepts `latest` as parameter. Only prometheus 2.x is supported |
| `prometheus_config_dir` | /etc/prometheus | Path to directory with prometheus configuration |
| `prometheus_db_dir` | /var/lib/prometheus | Path to directory with prometheus database |
| `prometheus_web_listen_address` | "0.0.0.0:9090" | Address on which prometheus will be listening |
| `prometheus_web_external_url` | "" | External address on which prometheus is available. Useful when behind reverse proxy. Ex. `http://example.org/prometheus` |
| `prometheus_storage_retention` | "30d" | Data retention period |
| `prometheus_storage_retention_size` | "0" | Data retention period by size |
| `prometheus_config_flags_extra` | {} | Additional configuration flags passed to prometheus binary at startup |
| `prometheus_alertmanager_config` | [] | Configuration responsible for pointing where alertmanagers are. This should be specified as list in yaml format. It is compatible with official [<alertmanager_config>](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alertmanager_config) |
| `prometheus_alert_relabel_configs` | [] | Alert relabeling rules. This should be specified as list in yaml format. It is compatible with the official [<alert_relabel_configs>](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alert_relabel_configs) |
| `prometheus_global` | { scrape_interval: 60s, scrape_timeout: 15s, evaluation_interval: 15s } | Prometheus global config. Compatible with [official configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#configuration-file) |
| `prometheus_remote_write` | [] | Remote write. Compatible with [official configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#<remote_write>) |
| `prometheus_remote_read` | [] | Remote read. Compatible with [official configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#<remote_read>) |
| `prometheus_external_labels` | environment: "{{ ansible_fqdn \| default(ansible_host) \| default(inventory_hostname) }}" | Provide map of additional labels which will be added to any time series or alerts when communicating with external systems |
| `prometheus_targets` | {} | Targets which will be scraped. Better example is provided in our [demo site](https://github.com/cloudalchemy/demo-site/blob/2a8a56fc10ce613d8b08dc8623230dace6704f9a/group_vars/all/vars#L8) |
| `prometheus_scrape_configs` | [defaults/main.yml#L58](https://github.com/cloudalchemy/ansible-prometheus/blob/ff7830d06ba57be1177f2b6fca33a4dd2d97dc20/defaults/main.yml#L47) | Prometheus scrape jobs provided in same format as in [official docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config) |
| `prometheus_config_file` | "prometheus.yml.j2" | Variable used to provide custom prometheus configuration file in form of ansible template |
| `prometheus_alert_rules` | [defaults/main.yml#L81](https://github.com/cloudalchemy/ansible-prometheus/blob/73d6df05a775ee5b736ac8f28d5605f2a975d50a/defaults/main.yml#L85) | Full list of alerting rules which will be copied to `{{ prometheus_config_dir }}/rules/ansible_managed.rules`. Alerting rules can be also provided by other files located in `{{ prometheus_config_dir }}/rules/` which have `*.rules` extension |
| `prometheus_alert_rules_files` | [defaults/main.yml#L78](https://github.com/cloudalchemy/ansible-prometheus/blob/73d6df05a775ee5b736ac8f28d5605f2a975d50a/defaults/main.yml#L78) | List of folders were ansible will look for files containing alerting rules which will be copied to `{{ prometheus_config_dir }}/rules/`. Files must have `*.rules` extension |
| `prometheus_static_targets_files` | [defaults/main.yml#L78](https://github.com/cloudalchemy/ansible-prometheus/blob/73d6df05a775ee5b736ac8f28d5605f2a975d50a/defaults/main.yml#L81) | List of folders were ansible will look for files containing custom static target configuration files which will be copied to `{{ prometheus_config_dir }}/file_sd/`. |


### Relation between `prometheus_scrape_configs` and `prometheus_targets`

#### Short version

`prometheus_targets` is just a map used to create multiple files located in "{{ prometheus_config_dir }}/file_sd" directory. Where file names are composed from top-level keys in that map with `.yml` suffix. Those files store [file_sd scrape targets data](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#file_sd_config) and they need to be read in `prometheus_scrape_configs`.

#### Long version

A part of *prometheus.yml* configuration file which describes what is scraped by prometheus is stored in `prometheus_scrape_configs`. For this variable same configuration options as described in [prometheus docs](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#<scrape_config>) are used.

Meanwhile `prometheus_targets` is our way of adopting [prometheus scrape type `file_sd`](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#<file_sd_config>). It defines a map of files with their content. A top-level keys are base names of files which need to have their own scrape job in `prometheus_scrape_configs` and values are a content of those files.

All this mean that you CAN use custom `prometheus_scrape_configs` with `prometheus_targets` set to `{}`. However when you set anything in `prometheus_targets` it needs to be mapped to `prometheus_scrape_configs`. If it isn't you'll get an error in preflight checks.

#### Example

Lets look at our default configuration, which shows all features. By default we have this `prometheus_targets`:
```
prometheus_targets:
  node:  # This is a base file name. File is located in "{{ prometheus_config_dir }}/file_sd/<<BASENAME>>.yml"
    - targets:              #
        - localhost:9100    # All this is a targets section in file_sd format
      labels:               #
        env: test           #
```
Such config will result in creating one file named `node.yml` in `{{ prometheus_config_dir }}/file_sd` directory.

Next this file needs to be loaded into scrape config. Here is modified version of our default `prometheus_scrape_configs`:
```
prometheus_scrape_configs:
  - job_name: "prometheus"    # Custom scrape job, here using `static_config`
    metrics_path: "/metrics"
    static_configs:
      - targets:
          - "localhost:9090"
  - job_name: "example-node-file-servicediscovery"
    file_sd_configs:
      - files:
          - "{{ prometheus_config_dir }}/file_sd/node.yml" # This line loads file created from `prometheus_targets`
```

## Example

### Playbook

```yaml
---
- hosts: all
  roles:
  - cloudalchemy.prometheus
  vars:
    prometheus_targets:
      node:
      - targets:
        - localhost:9100
        - demo.cloudalchemy.org:9100
        labels:
          env: demosite
```

### Demo site

We provide demo site for full monitoring solution based on prometheus and grafana. Repository with code and links to running instances is [available on github](https://github.com/cloudalchemy/demo-site) and site is hosted on [DigitalOcean](https://digitalocean.com).

### Defining alerting rules files

Alerting rules are defined in `prometheus_alert_rules` variable. Format is almost identical to one defined in[ Prometheus 2.0 documentation](https://prometheus.io/docs/prometheus/latest/configuration/template_examples/).
Due to similarities in templating engines, every templates should be wrapped in `{% raw %}` and `{% endraw %}` statements. Example is provided in [defaults/main.yml](defaults/main.yml) file.

## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip3 install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e py35-ansible28 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
