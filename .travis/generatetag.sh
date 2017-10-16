#!/bin/bash

git config --global user.email "soibot@sointeractive.pl"
git config --global user.name "soi-bot"
GIT_TAG=$([[ "$TRAVIS_COMMIT_MESSAGE" =~ ("Merge pull request".*/feature.*) ]] && git semver --next-minor || git semver --next-patch )
echo $GIT_TAG
git tag $GIT_TAG -a -m "Generated tag from TravisCI for build $TRAVIS_BUILD_NUMBER"
GIT_URL=$(git config --get remote.origin.url)
GIT_URL=${GIT_URL#*//}

git push https://${GH_TOKEN}:@${GIT_URL} --tags
