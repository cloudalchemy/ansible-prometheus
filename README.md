<p><img src="https://cdn.worldvectorlogo.com/logos/prometheus.svg" alt="prometheus logo" title="prometheus" align="right" height="60" /></p>

# Ansible Role: prometheus

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-prometheus.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-prometheus) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.prometheus-blue.svg)](https://galaxy.ansible.com/cloudalchemy/prometheus/) [![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-prometheus.svg)](https://github.com/cloudalchemy/ansible-prometheus/tags)

Deploy [Prometheus](https://github.com/prometheus/prometheus) monitoring system

## More info

An Ansible role that installs Prometheus Monitoring server.

## Requirements

- golang installed on deployer machine (same one where ansible is installed)

## Role Variables

Have a look at the [defaults/main.yml](defaults/main.yml) for variables that can be overridden.

Use the variable `prometheus_config_file` to provide your own prometheus.yml configuration in form of ansible template. This variable can be passed in form of file name or path to this file.

## Example

### Playbook

```yaml
---
- hosts: all
  become: yes
  roles:
  - cloudalchemy.prometheus
  vars:
    prometheus_targets:
      - targets:
        - demo.cloudalchemy.org:9100
        labels:
          env: demosite
          job: node
```

### Full site

We provide demo site for full monitoring solution based on prometheus and grafana. Repository with code is [available on github](https://github.com/cloudalchemy/demo-site) and site is hosted on DigitalOcean.

### Defining alerting rules files

Alerting rules are defined in `prometheus_alert_rules` variable. Format is almost identical to one defined in[ Prometheus 2.0 documentation](https://prometheus.io/docs/prometheus/latest/configuration/template_examples/).
Due to similarities in templating engines, every templates should be wrapped in `{% raw %}` and `{% endraw %}` statements. Example is provided in [defaults/main.yml](defaults/main.yml) file.

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
