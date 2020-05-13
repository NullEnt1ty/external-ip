import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

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
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license="MIT",
)
