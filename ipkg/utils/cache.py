import hashlib
import os
import sys
import typing
from pathlib import Path

CACHE_DIR = Path(
    os.environ.get("IPKG_CACHE_DIR", default=Path.home() / ".cache" / "ipkg")
)


def open_cache(args: list[str] = sys.argv[1:], encoding="utf-8") -> typing.TextIO:
    sha1 = hashlib.sha1(
        string=bytes(" ".join(args) + "\n", encoding=encoding)
    ).hexdigest()
    if CACHE_DIR:
        os.makedirs(CACHE_DIR, exist_ok=True)
        return open(file=CACHE_DIR / sha1, mode="w")
    else:
        return open(file=os.devnull, mode="w")


def export(cache: typing.TextIO, env: dict[str, str]) -> None:
    for name, value in env.items():
        print(f'export {name}="{value}";')
        print(f'export {name}="{value}"', file=cache)
