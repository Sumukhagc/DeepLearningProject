import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')
project_name='deepLearningProject'

list_of_files=[
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configurations.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/research.ipynb'
]

for filepath in list_of_files:
    filepath=Path(filepath)
    dirname,filename=os.path.split(filepath)

    if(dirname!=""):
        os.makedirs(dirname,exist_ok=True)
        logging.info("directory created "+dirname)
    if(not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
        logging.info("Created file "+filename)
    else:
        logging.info("already exists "+filename)        
        