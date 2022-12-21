import click
from rich import print

SHELL_ENV = """
# export IPKG="${IPKG:-"python entry_point.py"}"
# export IPKG_CACHE_DIR="${HOME}/.cache/ipkg"

function ipkg() {
  local sha1="$(sha1sum <<< "${*}" | awk '{ print $1 }')"
  local cache_path="${IPKG_CACHE_DIR}/${sha1}"
  if [[ -f ${cache_path} ]]; then
    local cache_hit=true
  fi
  if [[ ${cache_hit:-"false"} != "true" ]]; then
    ${IPKG:-"ipkg"} "${@}"
  fi
  if [[ -f ${cache_path} ]]; then
    source "${cache_path}"
  fi
}
"""


@click.command(name="shell-env")
def cmd_shell_env() -> None:
    print(SHELL_ENV)
