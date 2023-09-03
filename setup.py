from setuptools import find_packages, setup
from typing import List

hypen = "-e ."
def get_requirements(file_path:str)->List[str]:
    #this function will return the list of required libraries
    requirements = []
    with open(file_path) as file:
        requirements=file.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if hypen in requirements:
            requirements.remove(hypen)
    return requirements

setup(
    name='ML project',
    version=0.1,
    author='Paresh Mundale',
    author_email='pareshmundale07@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)