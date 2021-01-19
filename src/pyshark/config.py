import os

import iniconfig

import pyshark

CONFIG_PATH = os.path.join(os.path.dirname(pyshark.__file__), 'config.ini')


def get_config():
    return iniconfig.IniConfig(CONFIG_PATH)
