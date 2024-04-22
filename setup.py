from setuptools import setup

setup(name='mat_search',
      version='0.0.1',
      description='Material Search Package for Materials Project Platform',
      maintainer='Tirtha Vinchurkar',
      maintainer_email='tsvin642@gmail.com',
      license='MIT',
      packages=['mat_search'],
      entry_points={'console_scripts': ['mat = mat_search.main:main']},
      long_description='''\
This package provides utilities for searching materials based on their properties using the Materials Project platform. 
It allows users to specify various properties of materials, such as band gap, density, electronic and ionic properties, and more, and retrieve relevant materials data.
The package requires an API key to access the Materials Project Database. Users can specify the desired properties along with their minimum and maximum values, and the number of materials needed as output.
''')
