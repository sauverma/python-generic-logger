from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='generic_logging',
      version=version,
      description="Generic logging module",
      long_description="""\
Generic logging module""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='saurabh.verma',
      author_email='saurabhdec1988@gmail.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
