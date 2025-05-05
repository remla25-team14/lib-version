from setuptools import setup, find_packages

setup(
    name="libversion",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],
    author="REMLA Team 14",
    description="Shared library to expose version information",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)