from io import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tiktorch",
    version="21.6.24",
    description="Tiktorch client/server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilastik/tiktorch",
    author="ilastik Team",
    author_email="team@ilastik.org",
    classifiers=[  # Optional
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["tests"]),  # Required
    install_requires=[
        "inferno",
        "paramiko",
        "numpy",
        "pyyaml",
        "torch",
        "bioimageio.core @ git+ssh://git@github.com/bioimage-io/python-bioimage-io#egg=bioimageio.core",
        "bioimageio.torch @ git+ssh://git@github.com/bioimage-io/pytorch-bioimage-io#egg=bioimageio.torch",
    ],
    entry_points={"console_scripts": ["tiktorch=tiktorch.server.base:main"]},
    # extras_require={"test": ["pytest"]},
    project_urls={  # Optional
        "Bug Reports": "https://github.com/ilastik/tiktorch/issues",
        "Source": "https://github.com/ilastik/tiktorch/",
    },
)
