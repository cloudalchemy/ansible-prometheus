#!/usr/bin/env bash
#
# Description: Generate the next release version

set -uo pipefail

latest_tag="$(git semver)"
if [[ -z "${latest_tag}" ]]; then
  echo "ERROR: Couldn't get latest tag from git semver, try 'pip install git-semver'" 2>&1
  exit 1
fi

# Use HEAD if CIRCLE_SHA1 is not set.
now="${CIRCLE_SHA1:-HEAD}"

new_tag='none'
git_log="$(git log --format=%B "${latest_tag}..${now}")"

case "${git_log}" in
  *"[major]"*|*"[breaking change]"* )    new_tag=$(git semver --next-major) ;;
  *"[minor]"*|*"[feat]"*|*"[feature]"* ) new_tag=$(git semver --next-minor) ;;
  *"[patch]"*|*"[fix]"*|*"[bugfix]"* )   new_tag=$(git semver --next-patch) ;;
esac

echo "NEW_TAG=${new_tag}"
