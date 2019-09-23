"""Setup module for setuptools."""
from setuptools import setup, find_packages


setup(
    name='dependy',
    description='Project project dependency analysis.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords=['python', 'dependencies', 'graph', 'refactor', 'analyzer'],
    version='0.0.0',
    license='Apache Software License',
    author='Chris Gregory',
    author_email='christopher.b.gregory@gmail.com',
    url='https://github.com/gregorybchris/dependy',
    install_requires=[
        'pandas==0.24.2',
        'sentry-sdk==0.10.2'
    ],
    extras_require={
        'testing': [
            'pytest>=5.0.1'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',  # or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['tests'])
)