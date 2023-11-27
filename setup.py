from setuptools import find_packages, setup

setup(
    name='YOLO5',
    version='0.0.0',
    author='FraidoonJan',
    package_dir={"": "src"},
    packages=find_packages(where=".\src")
)
