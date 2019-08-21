#!/bin/bash

set -euo pipefail

if [ ! -d "./molecule/latest" ]; then
	tox
	exit 0
fi

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
	tox -- molecule test --all --destroy never
else
	tox -- molecule test -s default --destroy always
	if [ -d "./molecule/alternative" ]; then
		tox -- molecule test -s alternative --destroy never
	fi
fi
