from setuptools import setup


print('Please make sure to have python-dbus and python-gobject modules installed.')

setup(
    name='Lyvi',
    version='2.0-git',
    description='Command-line lyrics (and more!) viewer',
    long_description=open('README.txt').read(),
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
    install_requires=['Pillow', 'plyr', 'urwid', 'psutil'],
    package_data={'lyvi': ['data/pianobar/*']},
    data_files=[('share/man/man1', ['doc/lyvi.1'])]
)