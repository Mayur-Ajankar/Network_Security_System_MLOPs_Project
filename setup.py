 
"""
The setup.py file is a critical part of Python projects, 
especially when you want to distribute, install, or share your code as a package. 
It serves as the build script for setuptools (or sometimes distutils), and it tells Python how to install your package, 
what dependencies it needs, and additional metadata.

 """

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requiremments
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt",'r') as file:
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                # ignore empty lines and -e.

                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="Network_Security",
    version="0.0.1",
    author="mayur Ajankar",
    packages=find_packages(),
    install_requires=get_requirements()

     

)

