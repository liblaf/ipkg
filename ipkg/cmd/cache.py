import click
from rich import print

from ..utils.cache import CACHE_DIR
from ..utils.remove import remove


@click.command(name="clean")
def cmd_cache_clean():

    remove(CACHE_DIR)


@click.command(name="prefix")
def cmd_cache_prefix():

    print(CACHE_DIR)


@click.group(name="cache")
def cmd_cache() -> None:
    pass


cmd_cache.add_command(cmd=cmd_cache_clean)
cmd_cache.add_command(cmd=cmd_cache_prefix)
