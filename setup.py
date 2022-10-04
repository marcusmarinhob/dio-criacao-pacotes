from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="calculator",
    version="0.0.1",
    author="Marcus",
    author_email="my_email@myemail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcusmarinhob/dio-criacao-pacotes",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)