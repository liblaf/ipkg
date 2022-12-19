import subprocess

from ..log import get_logger

logger = get_logger()


def run(*args: str) -> None:
    logger.execute(msg="+ " + " ".join(args))
    subprocess.run(args=args)
