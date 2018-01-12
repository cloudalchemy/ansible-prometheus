#!/bin/bash
for i in ubuntu-molecule:16.04 debian-molecule:9 debian-molecule:8 centos-molecule fedora-molecule
do 
    docker pull paulfantom/$i &
done

wait
