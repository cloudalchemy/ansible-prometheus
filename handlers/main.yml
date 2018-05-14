---
- name: restart prometheus
  become: true
  systemd:
    daemon_reload: true
    name: prometheus
    state: restarted

- name: reload prometheus
  become: true
  systemd:
    name: prometheus
    state: reloaded
