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

None

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

Put the rules files to rules folder

Alerting rules are defined in the following syntax:
```yaml
ALERT <alert name>
  IF <expression>
  [ FOR <duration> ]
  [ LABELS <label set> ]
  [ ANNOTATIONS <label set> ]
```
Example Alertmanager rules files:
```yaml
# Alert for any instance that is unreachable for >5 minutes.
ALERT InstanceDown
  IF up == 0
  FOR 5m
  LABELS { severity = "page" }
  ANNOTATIONS {
    summary = "Instance {{ $labels.instance }} down",
    description = "{{ $labels.instance }} of job {{ $labels.job }} has been down for more than 5 minutes.",
  }
```

TODO
----

- Support every prometheus configuration option
- Tests
- Preflight checks
- Integrate alertmanager
- Fix README
