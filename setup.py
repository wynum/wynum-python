import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# What packages are required for this module to be executed?
REQUIRED = ['requests']

setuptools.setup(
    name="wynum",
    version="0.0.1",
    author="the-groot",
    author_email="suraj@wynum.com",
    description="Wynum API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # TODO add url
    url="", 
    packages=setuptools.find_packages(),
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License", # change later
        "Operating System :: OS Independent",
    ],
)