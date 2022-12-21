import logging
from pathlib import Path

import click

from . import __version__, pkg
from .cmd.cache import cmd_cache
from .cmd.install import cmd_install
from .cmd.list import cmd_list
from .cmd.load import cmd_load
from .cmd.remove import cmd_remove
from .cmd.shell_env import cmd_shell_env
from .cmd.unload import cmd_unload
from .log import install as log_install


@click.group(name="ipkg", context_settings={"show_default": True})
@click.version_option(version=__version__)
@click.option(
    "--log-level",
    type=click.Choice(
        choices=["OFF", "CRITICAL", "ERROR", "WARN", "INFO", "DEBUG", "NOTSET"],
        case_sensitive=False,
    ),
    default="INFO",
)
@click.option("--shell", default="bash")
def main(log_level: str, shell: str | Path):
    log_level = log_level.upper()
    if log_level == "OFF":
        log_install(77)
    else:
        log_install(logging._nameToLevel[log_level])
    pkg.SHELL = shell


main.add_command(cmd=cmd_cache)
main.add_command(cmd=cmd_install)
main.add_command(cmd=cmd_list)
main.add_command(cmd=cmd_load)
main.add_command(cmd=cmd_remove)
main.add_command(cmd=cmd_shell_env)
main.add_command(cmd=cmd_unload)


if __name__ == "__main__":
    main()
