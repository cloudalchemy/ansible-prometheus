# Ansible Role: prometheus 
An Ansible role that installs Prometheus Monitoring server with systemd.

## Requirements

All needed packages will be installed with this role. Minimal Ansible version - 2.0.

## Role Variables

Available main variables are listed below, along with default values:
```yaml
prometheus_version: 1.5.2
prometheus_gomaxprocs: "{{ ansible_processor_vcpus|default(ansible_processor_count) }}"
prometheus_user: prometheus
prometheus_group: prometheus
prometheus_service_name: prometheus

prometheus_global_scrape_interval: 15s
prometheus_global_evaluation_interval: 15s
prometheus_global_scrape_timeout: 10s
prometheus_self_scrape_interval: "{{ prometheus_global_scrape_interval }}"
prometheus_self_evaluation_interval: "{{ prometheus_global_scrape_interval }}"

prometheus_release_name: "prometheus-{{ prometheus_version }}.linux-amd64"

prometheus_root_dir: /opt/prometheus
prometheus_dist_dir: "{{ prometheus_root_dir }}/dist"
prometheus_bin_dir: "{{ prometheus_root_dir }}/current"
prometheus_rules_dir: "{{ prometheus_config_dir }}/rules"
prometheus_file_sd_config_dir: "{{ prometheus_config_dir }}/tgroups"

prometheus_config_dir: /etc/prometheus
prometheus_db_dir: /var/lib/prometheus

prometheus_rules_files: [alert.rules]

prometheus_web_listen_address: "0.0.0.0:9090"
prometheus_web_external_url: 'http://localhost:9090/'
prometheus_alertmanager_url: 'localhost:9093'

prometheus_config_flags:
  'config.file': '{{ prometheus_config_dir }}/prometheus.yml'
  'storage.local.path': '{{ prometheus_db_dir }}'
  'web.listen-address': '{{ prometheus_web_listen_address }}'
  'web.external-url': '{{ prometheus_web_external_url }}'
  'alertmanager.url': '{{ prometheus_alertmanager_url }}'

prometheus_config_flags_extra: {}
prometheus_pam_domain: "prometheus"
prometheus_pam_nofile_value: "1024"

prometheus_interface: ""
```

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

## Example Playbook
```yaml
---
- hosts: all
  gather_facts: yes

- hosts: all
  become: yes
  become_user: root
  roles:
  - role: ../../prometheus
    prometheus_external_labels:
      mon: orange

    prometheus_target_jobs:
      - job_name: 'node-exporter.{{ domain }}'
        port: 9100
        targets_group: all 
```

## TODO
