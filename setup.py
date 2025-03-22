'''
The setup.py file is an essential part of packaging and distributing python projects. It is used by setuptools (or distutils in older python versions) to define the configuration of your project ,such as its metadata ,dependencies ,and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_lst:List[str]=[]
    """ 
    Thiss function will return list of requiremnets.
    """
    try:
        with open('requirements.txt','r') as file:
            #read kines from the file
            lines=file.readlines()
            #skip spaces.
            for line in lines:
                requirement=line.strip()
                #skip lines and -e .
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file are not found")
                
    return requirement_lst       

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Harshita Shrimal",
    author_email="shrimalharshita2004@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
    
)