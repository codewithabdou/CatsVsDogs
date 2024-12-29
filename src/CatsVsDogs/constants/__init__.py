from pathlib import Path
import os

#path to root directory
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent

#path to config directory
CONFIG_FILE_PATH = Path( os.path.join(ROOT_DIR, "config", "config.yaml"))
PARAMS_FILE_PATH = Path( os.path.join(ROOT_DIR, "params.yaml"))


