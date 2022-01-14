import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wmath",
    version="0.1.0",
    author="wang606",
    author_email="wang__qing__hua@163.com",
    description="Another simple mathematical package in the world",
    LICENSE="MIT License", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wang606/wmath",
    project_urls={
        "Bug Tracker": "https://github.com/wang606/wmath/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
