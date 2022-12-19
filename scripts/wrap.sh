#!/usr/bin/bash
set -o errexit
set -o nounset
set -o pipefail

IPKG="${IPKG:-"ipkg"}"

function main() {
  ${IPKG} "${@}"
}

main "${@}"
