from setuptools import setuptools

setup(
    name = 'pv',
    version = '0.1',
    py_modules = ['pv'],
    install_requires=[
        'Click'
    ],
    entry_points='''
        [console_scripts]
        pv=pv:clic
    ''',
)
