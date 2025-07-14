from tkinter.constants import E
from chest.src.ChestCancerDetection import logger
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

import base64
import joblib
import yaml
import json
import os

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)

            logger.info(f"yaml file: {path_to_yaml} loaded successfully")

            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e