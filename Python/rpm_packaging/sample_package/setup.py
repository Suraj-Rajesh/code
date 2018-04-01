from setuptools import setup

setup(name='sample_package',
      version='1.0',
      description='A simple package generation example',
      author='Suraj Rajesh',
      entry_points = {
        'console_scripts': ['sample_package_exec=sample_package.command_line:main'],
      },
      packages=['sample_package'],
      zip_safe=False)

