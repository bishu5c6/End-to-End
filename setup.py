import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-Implementation"
AUTHOR_USER_NAME = "bishu5c6"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "pinnikabiswanth@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)





'''
from setuptools import setup, find_packages
from typing import List

PROJECT_NAME ="WINE_QUALITY_PREDICTION"
VERSION = "0.0.1"
DESCRIPTION = "END TO END ML PROJECT"
AUTHOR = "BISWANTH PINNIKA"
AUTHOR_EMAIL = "pinnikabiswanth@gmail.com"

REQUIREMENTS_FILE_NAME = 'requirements.txt'

HYPHON_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requriment_file:
        requriment_list = requriment_file.readlines()
        requriment_list = [ requriment_name.replace("\n", "") for requriment_name in requriment_list]

        if HYPHON_E_DOT in requriment_list:
            requriment_list.remove(HYPHON_E_DOT)
        return requriment_list


setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires = get_requirements_list()
     )
    
'''