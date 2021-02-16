from setuptools import setup

setup(
    name='motor_scraper',
    version='0.0.1',
    author="Lorence Cramwinckel",
    author_email="lorcr@live.nl",
    description='A simple scraper package',
    url="https://github.com/winckles/motor_scraper",
    py_modules=["package"],
    package_dir={'': 'scraper'},
    python_requires='>=3.6',
)
