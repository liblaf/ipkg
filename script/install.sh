#!/bin/bash
set -o errexit
set -o nounset
set -o pipefail

function exists() {
  command -v "${@}" > /dev/null 2>&1
}

function info() {
  if exists rich; then
    rich --print --style "bold bright_blue" "${*}"
  else
    echo -e -n "\x1b[1;94m"
    echo -n "${*}"
    echo -e "\x1b[0m"
  fi
}

function success() {
  if exists rich; then
    rich --print --style "bold bright_green" "${*}"
  else
    echo -e -n "\x1b[1;92m"
    echo -n "${*}"
    echo -e "\x1b[0m"
  fi
}

function copy() {
  mkdir --parents "$(realpath --canonicalize-missing "${2}/..")"
  cp --recursive "${1}" "${2}"
  success "COPY: ${1} -> ${2}"
}

function run() {
  info "+ ${*}"
  "${@}"
}

workspace="$(git rev-parse --show-toplevel || pwd)"
cd "${workspace}"

run bash "script/build.sh"
name="$(poetry version | awk '{ print $1 }')"
copy "dist/${name}" "${HOME}/.local/bin/${name}"
