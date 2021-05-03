import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fr:
    requires = fr.read()

setuptools.setup(
    name="ghlightning",  # Replace with your own username
    version="0.0.2",
    author="Nader Ahmed",
    author_email="nad3rahm3d@gmail.com",
    description="Github scrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/7azabet/lightning",
    project_urls={
        "Bug Tracker": "https://github.com/7azabet/lightning/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=requires,
    keywords='ghlightning github_scrapper scrapper github info NaderAhmed nad3rahm3d',
)
