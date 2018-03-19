#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages

setup(name='sins_bstick',
      version='1.0',
      description='Blinkstick Utilities',
      author='Michael Sinsabaugh',
      author_email='michael.sinsabaugh@gmail.com',
      packages=find_packages('src'),
      package_dir={'':'src'},
      install_requires=['blinkstick'],
      entry_points={ 'console_scripts': 
      		[
        	'rando=sins_bstick.bstick_random:main',
        	'off=sins_bstick.bstick_off:main',
          'bstick_color=sins_bstick.bstick_color:main',
          'cooler=sins_bstick.bstick_color:cooler',
          'hotter=sins_bstick.bstick_color:hotter',
          'heat_pulse=sins_bstick.bstick_color:heat_pulse',
          'set_color=sins_bstick.bstick_color:set_color',
          'police=sins_bstick.bstick_color:police',
          'rando_rainbow=sins_bstick.bstick_color:rando_rainbow'
    		],
		},
     )