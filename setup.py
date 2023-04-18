from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in it/__init__.py
from it import __version__ as version

setup(
	name="it",
	version=version,
	description="IT Oprations",
	author="Mohan Vanjare",
	author_email="iamvanjare@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
