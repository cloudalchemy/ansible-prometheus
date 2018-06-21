import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("dirs", [
    "/etc/prometheus",
    "/etc/prometheus/console_libraries",
    "/etc/prometheus/consoles",
    "/etc/prometheus/rules",
    "/etc/prometheus/file_sd",
    "/var/lib/prometheus"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/prometheus/prometheus.yml",
    "/etc/prometheus/console_libraries/prom.lib",
    "/etc/prometheus/consoles/prometheus.html",
    "/etc/systemd/system/prometheus.service",
    "/usr/local/bin/prometheus",
    "/usr/local/bin/promtool"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


@pytest.mark.parametrize("files", [
    "/etc/prometheus/rules/ansible_managed.rules",
    "/opt/prometheus/prometheus",
    "/opt/prometheus/promtool",
    "/opt/prometheus"
])
def test_absent(host, files):
    f = host.file(files)
    assert not f.exists


def test_service(host):
    s = host.service("prometheus")
    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    s = host.socket("tcp://0.0.0.0:9090")
    assert s.is_listening


def test_version(host):
    version = os.getenv('PROMETHEUS', "2.3.1")
    out = host.run("/usr/local/bin/prometheus --version").stderr
    assert "prometheus, version " + version in out
