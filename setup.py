import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pypvwatts',
    version="3.0.6",
    author='Miguel Paolino',
    author_email='mpaolino@gmail.com',
    url='https://github.com/mpaolino/pypvwatts',
    download_url='https://github.com/mpaolino/pypvwatts/archive/master.zip',
    description='Python wrapper for NREL PVWatts\'s API.',
    long_description=open('README.md').read(),
    packages=['pypvwatts'],
    provides=['pypvwatts'],
    requires=['requests'],
    install_requires=['requests>=2.32.3'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords='nrel pvwatts pypvwatts',
    license='MIT',
    python_requires=">=3.7",
)
