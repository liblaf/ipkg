import importlib

import click

from ..utils.name import module_name
from ..utils.prog_name import get_prog_name


@click.command(name="remove")
@click.pass_context
@click.argument("pkg")
@click.argument("args", nargs=-1)
def cmd_remove(ctx: click.Context, pkg: str, args: tuple[str]):
    pkg_module_name = module_name(pkg)
    module = importlib.import_module(name=f"ipkg.pkg.{pkg_module_name}.{ctx.info_name}")
    cmd: click.Command = module.main
    cmd.invoke(
        cmd.make_context(
            info_name=f"{get_prog_name()} {ctx.info_name} {pkg} --",
            args=list(args),
            show_default=ctx.show_default,
        )
    )
