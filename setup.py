import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read().splitlines()

setuptools.setup(
    name='nullent1ty-external-ip',
    version='1.0.1',
    author="Dominique Mattern",
    author_email="dominique@mattern.dev",
    description="Retrieve your external IPv4 address.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NullEnt1ty/external-ip",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
)
