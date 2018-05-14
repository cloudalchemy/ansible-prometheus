import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
DEFAULT_VERSION = "2.2.1"


@pytest.mark.parametrize("dirs", [
    "/opt/prom/etc",
    "/opt/prom/etc/rules",
    "/opt/prom/etc/file_sd",
    "/opt/prom/lib"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/opt/prom/etc/prometheus.yml",
    "/opt/prom/etc/rules/ansible_managed.rules",
    "/opt/prom/etc/file_sd/node.yml",
    "/opt/prom/etc/file_sd/docker.yml",
    "/etc/systemd/system/prometheus.service",
    "/usr/local/bin/prometheus",
    "/usr/local/bin/promtool"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_service(host):
    s = host.service("prometheus")
    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    s = host.socket("tcp://127.0.0.1:9090")
    assert s.is_listening


def test_version(host):
    v = os.getenv('PROMETHEUS', DEFAULT_VERSION)
    if int(v[0]) < 2:
        out = host.run("/usr/local/bin/prometheus -version").stdout
    else:
        out = host.run("/usr/local/bin/prometheus --version").stderr
    version = "prometheus, version " + v
    assert version in out
