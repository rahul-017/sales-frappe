from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sales_purchase/__init__.py
from sales_purchase import __version__ as version

setup(
	name="sales_purchase",
	version=version,
	description="MY CUSTOM APP",
	author="RAHUL.S",
	author_email="rahulitdata@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
