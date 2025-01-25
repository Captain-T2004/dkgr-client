from setuptools import setup, find_packages

setup(
    name='dkgr-client',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.0',
    ],
    author='Akshay Behl',
    author_email='akshaybehl231@gmail.com',
    description='Wrapper for dkgr backend',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)