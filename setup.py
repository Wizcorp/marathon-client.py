from distutils.core import setup

setup(
    name='marathon-client',
    version='0.1.1',
    author='Emilien Kenler',
    author_email='ekenler@wizcorp.jp',
    packages=['marathon'],
    scripts=['bin/marathon-client'],
    url='https://github.com/Wizcorp/marathon-client.py',
    license='LICENSE',
    description='Client for the Marathon scheduler.',
    install_requires=[
        "requests"
    ],
)
