#!/bin/bash
#
# Script downloads latest docker images from https://github.com/paulfantom/dockerfiles
# Requirements:
#   - docker
#
# Author: Pawel Krupa (@paulfantom)
#

for i in ubuntu-molecule:18.04 ubuntu-molecule:16.04 debian-molecule:9 debian-molecule:8 centos-molecule:7 fedora-molecule:27
do 
    docker pull paulfantom/$i &
done

wait
