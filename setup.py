import setuptools

with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wmath",
    version="0.0.5",
    author="wang606",
    author_email="wang__qing__hua@163.com",
    description="Another simple mathematical package in the world",
    LICENSE="MIT License", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://dev/null",
    project_urls={
        "Bug Tracker": "https://please/send/to/dev/null/i/check/that/place/every/night",
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
