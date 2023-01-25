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

function run() {
  info "+ ${*}"
  "${@}"
}

workspace="$(git rev-parse --show-toplevel || pwd)"
cd "${workspace}"

poetry install
name="$(poetry version | awk '{ print $1 }')"
pyinstaller --onefile --name "${name}" entry_point.py
