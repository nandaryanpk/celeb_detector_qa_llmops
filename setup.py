from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="celeb_detector_app",
    version="0.1",
    author="NRPK",
    packages=find_packages(),
    install_requires=requirements
)