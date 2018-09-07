from setuptools import setup

with open('pip_requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='Lyvi',
    version='2.0-git',
    description='Command-line lyrics (and more!) viewer',
    long_description=open('README.rst').read(),
    url='http://ok100.github.io/lyvi/',
    author='Ondrej Kipila',
    author_email='ok100@openmailbox.org',
    license='WTFPL',
    packages=['lyvi', 'lyvi.players'],
    entry_points={
        'console_scripts': [
            'lyvi = lyvi:main'
        ]
    },
    install_requires=install_requires,
    package_data={'lyvi': ['data/pianobar/*']},
    data_files=[('share/man/man1', ['doc/lyvi.1'])]
)

print('To enable MPRIS support, please make sure to have python-dbus and python-gobject modules installed.')
