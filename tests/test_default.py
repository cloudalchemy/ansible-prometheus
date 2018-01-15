from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_files(host):
    dirs = [
        "/opt/prometheus",
        "/etc/prometheus",
        "/etc/prometheus/rules",
        "/etc/prometheus/file_sd",
        "/var/lib/prometheus"
    ]
    files = [
        "/etc/prometheus/prometheus.yml",
        "/etc/prometheus/rules/ansible_managed.rules",
        "/etc/prometheus/file_sd/node.yml",
        "/etc/systemd/system/prometheus.service",
        "/opt/prometheus/prometheus",
        "/opt/prometheus/promtool"
    ]
    for directory in dirs:
        d = host.file(directory)
        assert d.is_directory
        assert d.exists
    for file in files:
        f = host.file(file)
        assert f.exists
        assert f.is_file


def test_service(host):
    s = host.service("prometheus")
    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    s = host.socket("tcp://127.0.0.1:9090")
    assert s.is_listening
