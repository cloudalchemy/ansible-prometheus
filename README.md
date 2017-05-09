# Ansible Role: prometheus 
An Ansible role that installs Prometheus Monitoring server on Ubuntu-based machines with systemd.

## Requirements

All needed packages will be installed with this role. Minimal Ansible version - 2.0.

## Role Variables

Available main variables are listed below, along with default values:
```yaml
prometheus_version: 1.5.2

prometheus_global_scrape_interval: 15s
prometheus_global_evaluation_interval: 15s
prometheus_global_scrape_timeout: 10s
prometheus_self_scrape_interval: "{{ prometheus_global_scrape_interval }}"
prometheus_self_evaluation_interval: "{{ prometheus_global_scrape_interval }}"

prometheus_root_dir: /opt/prometheus
prometheus_config_dir: /etc/prometheus
prometheus_pid_path: /var/run/prometheus.pid
prometheus_db_dir: /var/lib/prometheus

prometheus_web_listen_address: ":9090"
prometheus_alertmanager_url: 'localhost:9093'

prometheus_config_flags:
  'config.file': '{{ prometheus_config_dir }}/prometheus.yml'
  'storage.local.path': '{{ prometheus_db_dir }}'
  'web.listen-address': '{{ prometheus_web_listen_address }}'
  'alertmanager.url': '{{ prometheus_alertmanager_url }}'
```
All variables you can see [here](defaults/main.yml).

## Dependencies

This role doesn't have dependencies.

## Defining alerting rules files

Put the rules files to rules foleder

Alerting rules are defined in the following syntax:
```yaml
ALERT <alert name>
  IF <expression>
  [ FOR <duration> ]
  [ LABELS <label set> ]
  [ ANNOTATIONS <label set> ]
```

## Example Playbook
```yaml
---
- hosts: all
  become: yes
  become_user: root
  roles:
  - role: ../../prometheus
    prometheus_global_labels:
      a: b
    prometheus_target_jobs:
    - job_name: 'web-server'
      scrape_interval: '50s'
      scrape_timeout: '10s'
      targets:
        - "localhost:9090"
      labels:
        a: b
```

## TODO
