import click
from ishutils.common.run import run


@click.command()
def main() -> None:
    run(args=["gh", "auth", "login"])
    run(args=["gh", "auth", "setup-git"])
