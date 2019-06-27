import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# What packages are required for this module to be executed?
REQUIRED = ['requests']

setuptools.setup(
    name="wynum",
    version="0.0.2",
    author="patil-suraj",
    author_email="surajp815@gmail.com",
    description="Wynum API client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wynum/wynum-python",
    packages=setuptools.find_packages(),
    test_suite="test",
    install_requires=REQUIRED,
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers"
    ],
    project_urls={
        'Documentation': 'https://github.com/wynum/wynum-python',
        'Source': 'https://github.com/wynum/wynum-python',
    },
)
