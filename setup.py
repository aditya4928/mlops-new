from setuptools import setup, find_packages
from typing import List

def get_requirements():
    requirements = [] 
    with open("requirements.txt") as f:
        for line in f:                 # read each line
            req = line.strip()         # remove spaces/newlines
            if req and req != "-e .":  # skip empty lines & "-e ."
                requirements.append(req)
    return requirements              

setup(
    name="MLOPS-SECURITY",
    version="0.0.1",
    author="Aditya Pratap Singh",
    author_email="pratapaditya521@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)