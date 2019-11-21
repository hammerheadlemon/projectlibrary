from setuptools import setup, find_packages

setup(name="projectlibrary",
      version="0.1",
      description="Test Project Description",
      author="Mr Grant",
      install_requires=[
          'datamaps>=1.0.0'
      ],
      packages=find_packages()
      )
