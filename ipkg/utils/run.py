import subprocess

from ..log import get_logger


def run(*args: str, capture_output: bool = False) -> subprocess.CompletedProcess:
    logger = get_logger()
    logger.execute(msg="+ " + " ".join(args))
    return subprocess.run(args=args, capture_output=capture_output)
