import os

from setuptools import find_packages, setup, Extension

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):  # Stolen from txacme
    with open(os.path.join(HERE, *parts)) as f:
        return f.read()


setup(
    name='python-dev-docker-project',
    version='0.5.2.dev0',
    license='BSD-3-Clause',
    url='https://github.com/mavendataguy/jenkins_run',
    description='',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author='Aurangzeb Khan',
    author_email='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'test = src.test:main',
        ]
    }
)
