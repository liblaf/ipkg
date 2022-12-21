import os
from pathlib import Path

from httpie.core import main as https

from ..log import get_logger
from .confirm import confirm

logger = get_logger()


def download(
    url: str, output: str | Path, ask: bool = True, overwrite: bool = False
) -> None:
    output = Path(output)
    if output.exists():
        if ask:
            overwrite = confirm(
                message=f"Download: overwrite {output}", default=overwrite
            )
        if not overwrite:
            logger.skipped(f"Download: {url} -> {output}")
            return
    os.makedirs(name=output.parent, exist_ok=True)
    https(args=["https", "--body", "--download", "--output", str(output), url])
    logger.success(f"Download: {url} -> {output}")