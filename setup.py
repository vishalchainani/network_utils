import setuptools
from distutils.core import setup

setuptools.setup(
    name="network-utils",
    author="Vishal Chainani",
    author_email="vishal.chainani@gmail.com",
    description="A collection of network utilities",
    long_description="A collection of network utilities",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    setuptools_git_versioning={
        "enabled": True,
    },
    entry_points={
        'console_scripts': [
            'network-utils=network_utils.entry:cli_entry_point'
        ]
    },
    install_requires=[
        'argparse',
        'argcomplete',
        'setuptools-git-versioning>=2.0,<3',
    ],
)