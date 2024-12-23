import os
from pathlib import Path
from typing import Any, List
import base64
import yaml
import json
import joblib
from box import ConfigBox
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from CatsVsDogs.logging import logger
import binascii

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read and parse a YAML file.

    Args:
        path_to_yaml (Path): Path to the YAML file

    Returns:
        ConfigBox: Configuration as a ConfigBox object

    Raises:
        ValueError: If the YAML file is empty
        FileNotFoundError: If the file doesn't exist
        yaml.YAMLError: If the YAML syntax is invalid
    """
    try:
        logger.debug(f"Attempting to read YAML file: {path_to_yaml}")
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if not content:
                logger.warning("YAML file is empty, raising BoxValueError")
                yaml_file.close()
                raise BoxValueError("YAML file is empty")
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            yaml_file.close()
            return ConfigBox(content)
    except FileNotFoundError:
        logger.error(f"YAML file not found at: {path_to_yaml}")
        raise
    except yaml.YAMLError as e:
        logger.critical(f"Critical YAML parsing error: {e}")
        raise
    except Exception as e:
        logger.critical(f"Unexpected error reading YAML file: {e}")
        raise

@ensure_annotations
def create_directories(path_to_directories: List[Path], verbose: bool = True) -> None:
    """Create multiple directories if they don't exist.

    Args:
        path_to_directories (List[Path]): List of directory paths to create
        verbose (bool, optional): Whether to log directory creation. Defaults to True
    """
    logger.debug(f"Starting directory creation for {len(path_to_directories)} paths")
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory at: {path}")
        except PermissionError:
            logger.error(f"Permission denied creating directory: {path}")
            raise
        except Exception as e:
            logger.critical(f"Failed to create directory {path}: {e}")
            raise

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """Save data to a JSON file.

    Args:
        path (Path): Path to save the JSON file
        data (dict): Data to save
    """
    try:
        logger.debug(f"Attempting to save JSON file at: {path}")
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
            f.close()
        logger.info(f"JSON file saved successfully at: {path}")
    except PermissionError:
        logger.error(f"Permission denied saving JSON file: {path}")
        raise
    except TypeError as e:
        logger.error(f"JSON serialization error: {e}")
        raise
    except Exception as e:
        logger.critical(f"Unexpected error saving JSON file: {e}")
        raise

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Load data from a JSON file.

    Args:
        path (Path): Path to the JSON file

    Returns:
        ConfigBox: Data as class attributes
    """
    try:
        logger.debug(f"Attempting to load JSON file from: {path}")
        with open(path) as f:
            content = json.load(f)
            f.close()
        logger.info(f"JSON file loaded successfully from: {path}")
        return ConfigBox(content)
    except FileNotFoundError:
        logger.error(f"JSON file not found: {path}")
        raise
    except json.JSONDecodeError as e:
        logger.critical(f"JSON parsing error: {e}")
        raise
    except Exception as e:
        logger.critical(f"Unexpected error loading JSON file: {e}")
        raise

@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Save data to a binary file using joblib.

    Args:
        data (Any): Data to save
        path (Path): Path to save the binary file
    """
    try:
        logger.debug(f"Attempting to save binary file at: {path}")
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved successfully at: {path}")
    except PermissionError:
        logger.error(f"Permission denied saving binary file: {path}")
        raise
    except Exception as e:
        logger.critical(f"Failed to save binary file: {e}")
        raise

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load data from a binary file.

    Args:
        path (Path): Path to the binary file

    Returns:
        Any: Object stored in the file
    """
    try:
        logger.debug(f"Attempting to load binary file from: {path}")
        data = joblib.load(path)
        logger.info(f"Binary file loaded successfully from: {path}")
        return data
    except FileNotFoundError:
        logger.error(f"Binary file not found: {path}")
        raise
    except Exception as e:
        logger.critical(f"Failed to load binary file: {e}")
        raise

@ensure_annotations
def get_size(path: Path) -> str:
    """Get file size in KB.

    Args:
        path (Path): Path to the file

    Returns:
        str: Size in KB with formatting
    """
    try:
        logger.debug(f"Calculating file size for: {path}")
        size_in_kb = round(os.path.getsize(path) / 1024)
        logger.info(f"File size calculated: {size_in_kb} KB for {path}")
        return f"~ {size_in_kb} KB"
    except FileNotFoundError:
        logger.error(f"File not found while getting size: {path}")
        raise
    except Exception as e:
        logger.critical(f"Error calculating file size: {e}")
        raise

def decode_image(imgstring: str, filename: str) -> None:
    """Decode base64 string and save as image.

    Args:
        imgstring (str): Base64 encoded image string
        filename (str): Output filename
    """
    try:
        logger.debug(f"Attempting to decode base64 image to: {filename}")
        imgdata = base64.b64decode(imgstring)
        with open(filename, 'wb') as f:
            f.write(imgdata)
            f.close()
        logger.info(f"Image successfully decoded and saved as: {filename}")
    except binascii.Error:
        logger.error("Invalid base64 string provided")
        raise
    except Exception as e:
        logger.critical(f"Failed to decode image: {e}")
        raise

def encode_image_to_base64(image_path: str) -> bytes:
    """Encode image file to base64 string.

    Args:
        image_path (str): Path to the image file

    Returns:
        bytes: Base64 encoded image data
    """
    try:
        logger.debug(f"Attempting to encode image: {image_path}")
        with open(image_path, "rb") as f:
            encoded_data = base64.b64encode(f.read())
            f.close()
        logger.info(f"Image successfully encoded: {image_path}")
        return encoded_data
    except FileNotFoundError:
        logger.error(f"Image file not found: {image_path}")
        raise
    except Exception as e:
        logger.critical(f"Failed to encode image: {e}")
        raise