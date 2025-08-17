from setuptools import setup, find_packages
from typing import List

HYPENATION_PREFIX = '-e .'

def get_requirements(file_path:str) -> List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    """
    requirements = []

    with open(file_path) as file:
        requirements = file.readlines()
        requirements=[req.replace('\n', '') for req in requirements]
        if HYPENATION_PREFIX in requirements:
            requirements.remove(HYPENATION_PREFIX)
    return requirements

    
   

setup(
    name='MLProject',
    version='0.1.0',
    author='Vedant',
    author_email='vedantnavale02@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),







)