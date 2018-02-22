"""
pylint-badge
----

A small python module to generate pylint badges directly from command line
"""
from setuptools import setup


setup(
    name='pylint-badge',
    version='0.1',
    url='https://github.com/lucasventurasc/pylint-badge/',
    license='MIT',
    author='Lucas Ventura',
    author_email='lnventura@hotmail.com',
    description='A python module to generate pylint badges instantly',
    long_description=__doc__,
    py_modules=['pylint-badge'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
    ],
    classifiers=[
        'Environment :: Local',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Version Control'
    ]
)
