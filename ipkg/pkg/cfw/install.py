import typing
from pathlib import Path

import click
import requests

from ...utils.download import download
from ...utils.extract import extract
from ...utils.remove import remove
from ...utils.replace import replace
from ...utils.ubuntu.desktop import DesktopEntry, make_desktop_file
from .. import DOWNLOADS, OPT
from . import DOWNLOAD_URL, LOGO_URL, NAME, RELEASE_API


@click.command()
def main(version: typing.Optional[str] = None) -> None:
    if not version:
        json = requests.get(url=RELEASE_API).json()
        version = json["tag_name"]
    filename: str = f"Clash.for.Windows-{version}-x64-linux.tar.gz"
    url: str = f"{DOWNLOAD_URL}/{version}/{filename}"
    filepath: Path = DOWNLOADS / filename
    download(url=url, output=filepath)
    extract(src=filepath, dst=OPT)
    extract_dir = OPT / f"Clash for Windows-{version}-x64-linux"
    replace(src=extract_dir, dst=OPT / NAME)
    remove(path=extract_dir)
    logo_path = OPT / NAME / "logo.png"
    download(url=LOGO_URL, output=logo_path)
    make_desktop_file(
        slug="cfw",
        entry=DesktopEntry(
            Name="Clash for Windows",
            Exec=str(OPT / NAME / "cfw"),
            Icon=str(logo_path),
        ),
    )
