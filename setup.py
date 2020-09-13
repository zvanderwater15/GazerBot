#!/usr/bin/env python

from setuptools import setup

setup(name='gazerbot',
      version='1.0',
      description='Shoegaze Lyric Generator',
      author='Zoe vanderWater',
      author_email='zoe.van42@gmail.com',
      url='https://github.com/zvanderwater15/GazerBot',
      packages=['gazerbot'],
      install_requires=[
            'spotipy',
            'numpy',
            'lyricsgenius',
            'pytest'
      ], 
      scripts=['scripts/run.py']
)
