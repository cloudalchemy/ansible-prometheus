#!/bin/bash

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
	tox -- molecule test --all --destroy never
else
	tox -- molecule test -s default --destroy always
	tox -- molecule test -s alternative --destroy never
fi
