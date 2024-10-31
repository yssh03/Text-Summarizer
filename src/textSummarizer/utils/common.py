import os
import yaml
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
import logging


@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    """Read a YAML file and return a ConfigBox object."""

    try:
        with open(path) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty.")
    except Exception as e:
        print(e, "e")
        raise e


@ensure_annotations
def create_directory(path_to_directory: list, verbose=True):
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")


@ensure_annotations
def get_size(path_to_file: Path) -> str:
    size_in_kb = round(os.path.getsize(path_to_file)/1024)
    return f"{size_in_kb} KB"
