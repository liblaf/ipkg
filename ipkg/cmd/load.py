import importlib

import click

from ..utils.name import module_name
from ..utils.prog_name import get_prog_name


@click.command(name="load")
@click.argument("pkg")
@click.argument("args", nargs=-1)
def cmd_load(pkg: str, args: tuple[str]):
    pkg_module_name = module_name(pkg)
    pkg_load = importlib.import_module(name=f"ipkg.pkg.{pkg_module_name}.load")
    pkg_load.main.main(args=args, prog_name=f"{get_prog_name()} load {pkg} --")
