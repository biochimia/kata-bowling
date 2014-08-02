# vim: set fileencoding=utf-8 :

from setuptools import setup

setup(
    name='bowling',
    description='Calculate the score for American Ten-Pin Bowling',

    author='João Abecasis',
    author_email='joao@abecasis.name',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    license='MIT',

    tests_require=['nose'],
    test_suite='nose.collector',
)
