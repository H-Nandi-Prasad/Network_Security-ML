'''
The setup.py file is essential part of packaging and distributing python Projects.
It is used by the setup tools (or distutils in older Python versions) to define 
the configuration of your projects, such as metadata, dependencies, and more 
'''

from setuptools import find_packages,setup
from typing import List


requirement_lst:List[str]=[]

def get_requirements():
    try:
        with open('requirements.txt') as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError :
        print("Requirement.txt is not found")
    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Nandi Prasad",
    author_email="nandiprasadhyati@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)