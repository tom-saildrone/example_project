from setuptools import setup

setup(
    name='example_project',
    version='0.9',
    packages=['example_project'],
    install_requires=['requests'],
    package_dir={'': 'python'},
    url='',
    license='',
    author='Tom Matthias',
    author_email='tom@saildrone.com',
    description='An example project that does...something.',
    entry_points={'console_scripts': []}
)
