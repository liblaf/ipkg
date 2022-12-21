import importlib.util
import pkgutil
from importlib.machinery import ModuleSpec

import click
from rich import print
from rich.columns import Columns
from rich.tree import Tree

from ..utils.name import package_name


def get_list(spec: ModuleSpec) -> list[str]:
    names: list[str] = list()
    for module in pkgutil.iter_modules(path=spec.submodule_search_locations):
        names.append(package_name(mod_name=module.name))
    return names


def get_tree(spec: ModuleSpec) -> Tree:
    names: Tree = Tree(spec.name.removeprefix("ipkg."))
    for module in pkgutil.iter_modules(path=spec.submodule_search_locations):
        tree_node = names.add(package_name(mod_name=module.name))
        if not module.ispkg:
            continue
        sub_spec = importlib.util.find_spec(name=f"{spec.name}.{module.name}")
        assert sub_spec
        for sub_module in pkgutil.iter_modules(
            path=sub_spec.submodule_search_locations
        ):
            tree_node.add(package_name(sub_module.name))
    return names


@click.command(name="list")
@click.option("--tree", is_flag=True)
@click.argument("pkg", required=False, default="")
def cmd_list(tree: bool, pkg: str):
    if pkg:
        spec = importlib.util.find_spec(name=f"ipkg.pkg.{pkg}")
        if not spec:
            raise LookupError(f'Package "{pkg}" Not Found!')
    else:
        spec = importlib.util.find_spec(name="ipkg.pkg")
    assert spec
    if tree:
        names = get_tree(spec=spec)
        print(names)
    else:
        names = get_list(spec=spec)
        print(Columns(names, expand=False, equal=True))
