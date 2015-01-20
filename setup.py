from setuptools import setup

SETUP_INFO = dict(
    name='commondata.eg',
    version='0.0.1',
    install_requires=['commondata'],
    description="Common data about Egypt",
    license='BSD license',
    test_suite='tests',
    author='Mahmoud Mamdouh',
    author_email='sharedup@gmail.com',
    url="https://github.com/ExcellentServ/commondata-eg",
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: BSD license
Natural Language :: English
Natural Language :: Arabic
Operating System :: OS Independent""".splitlines())

SETUP_INFO.update(long_description=file('README.rst').read())

SETUP_INFO.update(packages=[str(n) for n in """
commondata.eg
""".splitlines() if n])

SETUP_INFO.update(namespace_packages=['commondata'])

if __name__ == '__main__':
    setup(**SETUP_INFO)
