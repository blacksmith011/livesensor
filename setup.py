from setuptools import find_packages,setup

def get_requirement()->list[str]:
    requirement_list = list[str] =[]

    return requirement_list

setup(
    name='sensor',
    version="0.0.1",
    author="Aryan",
    author_email="aryanceo888@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement()
)