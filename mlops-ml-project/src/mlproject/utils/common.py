import os
from box.exceptions import BoxValueError
import yaml
from src.mlproject import logger
import json
import joblib
from ensure import ensure_annotations # esto es un decorador que hace restrictivo el tipado de python
# si no se corresponde el tipado a lo que se da de input o output, da error
from box import ConfigBox # esto es una clase que permite a los diccionarios llamar a sus valores por dict.key
# no solo por dict['key'] Esto es util para las configuraciones en yaml
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: configbox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")

            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): List of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. defaults to false.
    
    """
    for path in path_to_directories:
        os.makedirs(path, exists_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data
    
    Args:
        path (Path): path to json data
        data (dict): data to be saved in json file
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file data
    
    Args:
        path (Path): path to json file
    
    returns:
        ConfigBox: data as class atributes instead of dict 
    """

    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from: {path}")
    
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file
    
    Returns:
        Any: object stored in the file
    
    """

    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")

    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    
    Args:
        path (Path): path to file
    Returns:
        str: size in kB
    """

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"








