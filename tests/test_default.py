from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(host):
    present = [
        "/opt/prometheus",
        "/etc/prometheus",
        "/etc/prometheus/rules",
        "/etc/prometheus/file_sd",
        "/var/lib/prometheus"
    ]
    if present:
        for directory in present:
            d = host.file(directory)
            assert d.is_directory
            assert d.exists


def test_files(host):
    present = [
        "/etc/prometheus/prometheus.yml",
        "/etc/systemd/system/prometheus.service",
        "/opt/prometheus/prometheus",
        "/opt/prometheus/promtool"
    ]
    if present:
        for file in present:
            f = host.file(file)
            assert f.exists
            assert f.is_file


def test_service(host):
    present = [
        "prometheus"
    ]
    if present:
        for service in present:
            s = host.service(service)
            assert s.is_enabled


def test_socket(host):
    present = [
        "tcp://127.0.0.1:9090"
    ]
    for socket in present:
        s = host.socket(socket)
        assert s.is_listening
