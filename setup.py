'''
Setuptools and the maintainers of thousands of other packages are working with 
Tidelift to deliver one enterprise subscription that covers all of the open source you use.
'''
from setuptools import find_packages,setup

'''
Typing Package
'''
from typing import List

#Variables 
REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
    requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
    
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list

setup(
    name = "mushroom_classification",
    version = "0.0.1",
    author = "Ayush Poojari",
    author_email = "ayushp.b11@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)
