from click.utils import _detect_program_name


def get_prog_name() -> str:
    return _detect_program_name()
