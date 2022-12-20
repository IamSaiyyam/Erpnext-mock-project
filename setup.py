from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in erpnext_mock_project/__init__.py
from erpnext_mock_project import __version__ as version

setup(
	name="erpnext_mock_project",
	version=version,
	description="Here I\'ll practice the mock project",
	author="Saiyyam Chhetri",
	author_email="saiyyam.d@promantia.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
