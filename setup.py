from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def read_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements.

    Args:
        file_path (str): The path to the requirements file.

    Returns:
        List[str]: A list of requirements.
    """
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.read().splitlines()
            requirements = [req.strip() for req in requirements if req.strip()]
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        requirements = []
    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    description='Machine learning project',
    author='Zia ul islam Mughal',
    author_email='ziamughal132@gmail.com',
    url='https://github.com/ziaulislammughal/ML-end-to-end-.git',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt')
)