#!/usr/bin/bash
set -o errexit
set -o nounset
set -o pipefail

export IPKG="${IPKG:-"python entry_point.py"}"
export IPKG_CACHE_DIR="${HOME}/.cache/ipkg"

function ipkg() {
  local sha1sum="$(sha1sum <<< "${*}" | awk '{ print $1 }')"
  local cache_path="${IPKG_CACHE_DIR}/${sha1sum}"
  if [[ -f ${cache_path} ]]; then
    local cache_hit=true
  fi
  if [[ ${cache_hit:-"false"} != "true" ]]; then
    ${IPKG} "${@}"
  fi
  if [[ -f ${cache_path} ]]; then
    source "${cache_path}"
  fi
}

ipkg "${@}"
