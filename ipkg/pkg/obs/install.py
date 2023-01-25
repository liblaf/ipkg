import click
from ishutils.common.run import run


@click.command()
def main() -> None:
    run(args=["sudo", "add-apt-repository", "ppa:obsproject/obs-studio"])
    run(args=["sudo", "apt", "update"])
    run(args=["sudo", "apt", "install", "ffmpeg", "obs-studio"])
