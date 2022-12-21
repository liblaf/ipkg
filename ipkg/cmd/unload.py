import importlib

import click

from ..utils.name import module_name
from ..utils.prog_name import get_prog_name


@click.command(name="unload")
@click.argument("pkg")
@click.argument("args", nargs=-1)
def cmd_unload(pkg: str, args: tuple[str]):
    pkg_module_name = module_name(pkg)
    pkg_unload = importlib.import_module(name=f"ipkg.pkg.{pkg_module_name}.unload")
    pkg_unload.main.main(args=args, prog_name=f"{get_prog_name()} unload {pkg} --")
