from setuptools import find_packages,setup
from typing import List

def get_reqirements(file_path:str)->list[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path)  as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]




setup(
name='ml_project',
version='0.0.1',
author='om'
author_email='ombhosale0909@gmail.com'
packages=find_packages(),
install_requires=get_requirements('requirement.txt'),
)