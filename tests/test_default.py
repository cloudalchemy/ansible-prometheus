from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_directories(File):
    present = [
        "/opt/prometheus",
        "/etc/prometheus",
        "/etc/prometheus/rules",
        "/etc/prometheus/file_sd",
        "/var/lib/prometheus"
    ]
    if present:
        for directory in present:
            d = File(directory)
            assert d.is_directory
            assert d.exists


def test_files(File):
    present = [
        "/etc/prometheus/prometheus.yml",
        "/etc/systemd/system/prometheus.service",
        "/opt/prometheus/prometheus",
        "/opt/prometheus/promtool"
    ]
    if present:
        for file in present:
            f = File(file)
            assert f.exists
            assert f.is_file


def test_service(Service):
    present = [
        "prometheus"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_enabled


def test_socket(Socket):
    present = [
        "tcp://127.0.0.1:9090"
    ]
    for socket in present:
        s = Socket(socket)
        assert s.is_listening
