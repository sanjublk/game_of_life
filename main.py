import argparse
import logging

logger = None


def parse_args():
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument(
        "-d", "--debug", help="Enable debug logging", action="store_true"
    )
    return parser.parse_args()


def configure_logger(level=logging.INFO):
    global logger
    logger = logging.getLogger("game of life")
    logger.setLevel(level)
    screen_handler = logging.StreamHandler()
    screen_handler.setLevel(level)
    formatter = logging.Formatter(
            "[%(levelname)s] : %(lineno)d : %(message)s"
            )
    screen_handler.setFormatter(formatter)
    logger.addHandler(screen_handler)

def main():
    args = parse_args()
    if args.debug:
        configure_logger(logging.DEBUG)
    else:
        configure_logger(logging.INFO)