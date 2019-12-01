import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flashtool",
    version="0.0.6",
    author="Haoming Jiang",
    author_email="jianghm.ustc@gmail.com",
    description="A few ready-to use python tools for machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gatech-Flash/FlashPythonToolbox",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
