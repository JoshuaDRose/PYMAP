from setuptools import setup, find_packages

setup(
    name="PYMAP",
    version="0.0.1",
    author="Joshua Rose",
    author_email="joshuarose099@gmail.com",
    description="An application that is a python music player.",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["PYMAP = src.__main__:main"]},
)
