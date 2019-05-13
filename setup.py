# Copyright Alan (AJ) Pryor, Jr. 2018

from setuptools import setup, find_packages

setup(name='py2ng',
      author='Alan "AJ" Pryor, Jr.',
      author_email='apryor6@gmail.com',
      version='0.1.2',
      description='Convert Marshmallow schemas to TypeScript interfaces',
      ext_modules=[],
      packages=find_packages(),
      install_requires=['Flask-RESTful>=0.3.7'],
      scripts=['bin/py2ng']
      )
