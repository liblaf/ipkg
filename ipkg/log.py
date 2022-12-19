import logging
import typing

SKIPPED = logging.INFO + 1
EXECUTE = SKIPPED + 1
SUCCESS = EXECUTE + 1
TIPS = SUCCESS + 1


class Logger(logging.Logger):
    def skipped(self, msg, *args, **kwargs):
        if self.isEnabledFor(SKIPPED):
            self._log(SKIPPED, "[logging.level.skipped]" + msg + "[/]", args, **kwargs)

    def execute(self, msg, *args, **kwargs):
        if self.isEnabledFor(EXECUTE):
            self._log(EXECUTE, "[logging.level.execute]" + msg + "[/]", args, **kwargs)

    def success(self, msg, *args, **kwargs):
        if self.isEnabledFor(SUCCESS):
            self._log(SUCCESS, "[logging.level.success]" + msg + "[/]", args, **kwargs)

    def tips(self, msg, *args, **kwargs):
        if self.isEnabledFor(TIPS):
            self._log(TIPS, "[logging.level.tips]" + msg + "[/]", args, **kwargs)


def install_log_level(level: int, name: str):
    setattr(logging, name, level)
    logging._levelToName[level] = name
    logging._nameToLevel[name] = level
    pass


def install(level: int = logging.NOTSET):
    logging.setLoggerClass(Logger)
    install_log_level(level=TIPS, name="TIPS")
    install_log_level(level=SUCCESS, name="SUCCESS")
    install_log_level(level=EXECUTE, name="EXECUTE")
    install_log_level(level=SKIPPED, name="SKIPPED")
    if level > logging.CRITICAL:
        get_logger().disabled = True
    else:
        from rich.console import Console
        from rich.logging import RichHandler
        from rich.pretty import install as pretty_install
        from rich.theme import Theme
        from rich.traceback import install as traceback_install

        theme = Theme(
            {
                "logging.level.skipped": "dim",
                "logging.level.execute": "bold blue",
                "logging.level.success": "bold green",
                "logging.level.tips": "bold cyan",
            }
        )
        console = Console(theme=theme, stderr=True)
        pretty_install(console=console)
        traceback_install(console=console)
        logging.basicConfig(
            level=level,
            format="%(message)s",
            handlers=[RichHandler(console=console, markup=True)],
        )
    logging.root = logging.getLogger("main")


def get_logger(name: str = "main", level: int = logging.NOTSET) -> Logger:
    return typing.cast(Logger, logging.getLogger(name))
