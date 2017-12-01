<p><img src="https://cdn.worldvectorlogo.com/logos/prometheus.svg" alt="prometheus logo" title="prometheus" align="right" height="60" /></p>

Ansible Role: prometheus
========================

[![Build Status](https://travis-ci.org/cloudalchemy/ansible-prometheus.svg?branch=master)](https://travis-ci.org/cloudalchemy/ansible-prometheus) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.prometheus-blue.svg)](https://galaxy.ansible.com/cloudalchemy/prometheus/) [![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-prometheus.svg)](https://github.com/cloudalchemy/ansible-prometheus/tags)

Deploy Prometheus monitoring system

More info
---------

An Ansible role that installs Prometheus Monitoring server.

Requirements
------------

- golang installed on deployer machine (same one where ansible is installed)

Role Variables
--------------

Have a look at the [defaults/main.yml](defaults/main.yml) for variables that can be overridden.

Use the variable prometheus_custom_config_path to provide your own prometheus.yml configuration. This is useful when you want to discard the default configuration provided by this Ansible role. The role first looks for the file prometheus.yml.j2 file in provided path. If not found, the role uses the default configuration.

Example usage
-------------

```yaml
---
- hosts: all
  gather_facts: yes

- hosts: all
  become: yes
  become_user: root
  roles:
  - role:
      - cloudalchemy.prometheus
  vars:
    prometheus_external_labels:
      monitoring: a
    prometheus_targets:
      - targets:
        - host_ip_or_domain:port
        labels:
          env: environment_name_usually_domain_name
          job: node
```

Defining alerting rules files
-----------------------------

Alerting rules are defined in `prometheus_alert_rules` variable. Format is almost identical to one defined in[ Prometheus 2.0 documentation](https://prometheus.io/docs/prometheus/latest/configuration/template_examples/).
Due to similarities in templating engines, every templates should be wrapped in `{% raw %}` and `{% endraw %}` statements. Example is provided in [defaults/main.yml](defaults/main.yml) file.

TODO
----

- Support every prometheus configuration option
- Tests
- Preflight checks
- Better README
