#!/bin/bash

function success {
  GIT_TAG=$(git semver)
  echo $GIT_TAG
  if [ "$TRAVIS_PULL_REQUEST" != "false" ]
  then
    MESSAGE="Travis [build no. ${TRAVIS_BUILD_NUMBER}](travis-ci.org/${TRAVIS_REPO_SLUG}/builds/${TRAVIS_BUILD_ID}) has finished successfully. Pull request no. ${TRAVIS_PULL_REQUEST} opened by ${GIT_COMMITER} can be found [here](https://github.com/${TRAVIS_REPO_SLUG}/pull/${TRAVIS_PULL_REQUEST})."
  else
    MESSAGE="Travis [build no. ${TRAVIS_BUILD_NUMBER}](travis-ci.org/${TRAVIS_REPO_SLUG}/builds/${TRAVIS_BUILD_ID}) has finished successfully. Tag [${GIT_TAG}](https://github.com/${TRAVIS_REPO_SLUG}/releases/tag/${GIT_TAG}) was pushed to master by ${GIT_COMMITER}."
  fi
  echo $MESSAGE
}

function failure {
  if [ "$TRAVIS_PULL_REQUEST" != "false" ]
  then
    MESSAGE="Travis [build no. ${TRAVIS_BUILD_NUMBER}](travis-ci.org/${TRAVIS_REPO_SLUG}/builds/${TRAVIS_BUILD_ID}) has failed. Pull request no. ${TRAVIS_PULL_REQUEST} opened by ${GIT_COMMITER} can be found [here](https://github.com/${TRAVIS_REPO_SLUG}/pull/${TRAVIS_PULL_REQUEST})."
  else
    MESSAGE="Travis [build no. ${TRAVIS_BUILD_NUMBER}](travis-ci.org/${TRAVIS_REPO_SLUG}/builds/${TRAVIS_BUILD_ID}) has failed. Please check for problems on branch [master](https://github.com/${TRAVIS_REPO_SLUG}/tree/master) which was pushed by ${GIT_COMMITER} on repo [${TRAVIS_REPO_SLUG}](https://github.com/${TRAVIS_REPO_SLUG})."
  fi
}

if [ -z "$MM_WEBHOOK" ]
then
  echo "MM_WEBHOOK variable is not set!"
  exit 0
fi

GIT_COMMITER=$(git show -s --pretty=%an)
echo $GIT_COMMITER
if [ "$TRAVIS_TEST_RESULT" == "0" ]
then
  success
  COLOR="#00FF00"
else
  failure
  COLOR="#FF0000"
fi

curl -X POST --data-urlencode "payload={\"username\": \"soi\", \"attachments\": [{ \"color\": \"$COLOR\", \"text\": \"$MESSAGE\" }], \"icon_url\": \"https://maxcdn.icons8.com/office/PNG/512/Programming/bot_80-512.png\"}" "${MM_WEBHOOK}"
