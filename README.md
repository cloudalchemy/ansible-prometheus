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

## Example Playbook
```yaml
- hosts: monitoring
  roles:
    - { role: prometheus }
```
You should create another config parts of main file inside `{{ playbook_dir }}/files/config_parts`.  
You can use Ansible [assembly](http://docs.ansible.com/ansible/assemble_module.html) and config parts should have alphabethical order. For example `2-static_sd.yml`:
```yaml
  - job_name: "files_sd"
    scrape_interval: 15s
    file_sd_configs:
      - files:
        - '/etc/prometheus/tgroups/*.json'
        - '/etc/prometheus/tgroups/*.yml'
        - '/etc/prometheus/tgroups/*.yaml'
        refresh_interval: '5m'
```

## TODO
