from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    "this function will return lst of _requirements"
    requirements =[]
    with open(file_path)as file_obj:
        requirements=file_obj.readlines()
        [req.replace("/n","")for req in requirements]
        

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

            return requirements


setup(
    name ="ML_Project",
    version="0.0.1",
    author = 'tanwish naik',
    author_email='tanwiish.naiik@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')

)