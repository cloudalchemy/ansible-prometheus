import pytest
import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')
DEFAULT_VERSION = "2.2.1"


@pytest.mark.parametrize("dirs", [
    "/etc/prometheus",
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
    "/etc/prometheus/rules/ansible_managed.rules",
    "/etc/prometheus/file_sd/node.yml",
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
      out = host.run("/usr/local/bin/prometheus -version").stderr
    else:
      out = host.run("/usr/local/bin/prometheus --version").stderr
    version = "prometheus, version " + v
    assert version in out
