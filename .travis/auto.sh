#!/bin/bash

git clone https://github.com/paulfantom/travis-helper.git helper

chmod +x helper/*

bash helper/tagger.sh 
bash helper/changelog.sh

exit 0
