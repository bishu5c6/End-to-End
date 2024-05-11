from setuptools import find_packages, setup
from typing import List

PROJECT_NAME ="Wine_Quality_Prediction"
VERSION = "0.0.1"
DESCRIPTION = "END TO END ML PROJECT"
AUTHOR = "bishu5c6"
AUTHOR_EMAIL = "pinnikabiswanth@gmail.com"

REQUIREMENTS_FILE_NAME = 'requirements.txt'


HYPHON_E_DOT = "-e ."

def get_requriments(filepath: str) -> List[str]:
    requirements = []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [ i.replace("\n", "") for i in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)


setup(name=PROJECT_NAME, 
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url = f"https://github.com/{AUTHOR}",
      packages=find_packages(),
      install_requires = get_requriments("requirements.txt")
     )