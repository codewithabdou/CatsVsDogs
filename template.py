import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = 'Cats-VS-Dogs'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files :
    OSPath = Path(filepath)
    filedir , filename = os.path.split(OSPath)

    if filedir != "" and (not os.path.exists(filedir)):
        os.makedirs(filedir, exist_ok=True)
        logging.info("Created directory at {filedir} for {filename}")
    
    if (not os.path.exists(OSPath)) or (os.path.getsize(OSPath)):
        with open(OSPath, 'w') as f:
            pass
            logging.info(f"Created file at {OSPath}")
    else:
        logging.info(f"File already exists at {OSPath}. Skipping creation.")

        