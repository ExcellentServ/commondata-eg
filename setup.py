from setuptools import setup

SETUP_INFO = dict(
    name='commondata.ee',
    version='0.0.1',
    install_requires=['commondata'],
    description="Common data about Estonia",
    license='BSD license',
    test_suite='tests',
    author='Luc Saffre',
    author_email='luc.saffre@gmail.com',
    url="http://commondata.lino-framework.org",
    classifiers="""\
Programming Language :: Python
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: BSD license
Natural Language :: English
Natural Language :: Estonian
Operating System :: OS Independent""".splitlines())

SETUP_INFO.update(long_description=file('README.rst').read())

SETUP_INFO.update(packages=[str(n) for n in """
commondata.ee
""".splitlines() if n])

SETUP_INFO.update(namespace_packages=['commondata'])

if __name__ == '__main__':
    setup(**SETUP_INFO)
