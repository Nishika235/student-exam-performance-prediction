from setuptools import find_packages,setup
from typing import List



Hypen_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n"," ") for req in requirements] 
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    return requirements

setup(
    name="ml_projects",
    version="0.0.1",
    description="Collection of Machine Learning projects",
    author="Nishika",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)