"""Module for config file setup and settings."""
import configparser
import pathlib


def load_config() -> configparser.ConfigParser:
    """Loads the app config file."""
    path = str(pathlib.Path().absolute())
    config = configparser.ConfigParser()
    config.read(f'{path}/config.ini')
    return config
