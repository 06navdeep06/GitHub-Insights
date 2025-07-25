from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gh-insights",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool to fetch and analyze GitHub repository statistics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gh-insights",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "gh-insights=gh_insights.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
