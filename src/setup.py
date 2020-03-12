from distutils.core import setup

setup(
    name='automatic-octo-utils',
    version='0.1.0',
    author='Bruno Paes',
    author_email='brunopaes05@gmail.com',
    packages=['mooncake'],
    scripts=['mooncake/__init__.py'],
    url='https://github.com/Brunopaes/Miek',
    license='MIT',
    description='Utils functions',
    long_description=open('README.md').read()
)
