
from setuptools import setup, find_packages

setup(
    name='cliweather_subhan',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click', 'requests','asyncio','aiohttp'
    ],
    entry_points='''
        [console_scripts]
        cliweather=main:cli
    ''',
)