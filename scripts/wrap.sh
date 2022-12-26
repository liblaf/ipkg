#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

export IPKG="python entry_point.py"
export IPKG_CACHE_DIR="${HOME}/.cache/ipkg"

function ipkg() {
  local sha1="$(sha1sum <<< "${*}" | awk '{ print $1 }')"
  local cache_path="${IPKG_CACHE_DIR}/${sha1}"
  if [[ -f ${cache_path} ]]; then
    local cache_hit=true
  fi
  if [[ ${cache_hit:-"false"} != "true" ]]; then
    ${IPKG:-command ipkg} "${@}"
  fi
  if [[ -f ${cache_path} ]]; then
    source "${cache_path}"
  fi
}

ipkg "${@}"
