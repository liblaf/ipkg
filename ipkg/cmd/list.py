import importlib.util
import pkgutil

import click
from rich import print
from rich.columns import Columns

from ..utils.name import package_name


@click.command(name="list")
@click.argument("pkg", required=False, default="")
def cmd_list(pkg: str = ""):
    if pkg:
        pkg_spec = importlib.util.find_spec(name=f"ipkg.pkg.{pkg}")
        if not pkg_spec:
            raise LookupError(f'Package "{pkg}" not found!')
    else:
        pkg_spec = importlib.util.find_spec(name="ipkg.pkg")
    assert pkg_spec
    pkgs: list[str] = list()
    for module in pkgutil.iter_modules(path=pkg_spec.submodule_search_locations):
        pkgs.append(package_name(module.name))
    pkgs = list(set(pkgs))
    print(Columns(pkgs, expand=False, equal=True))
