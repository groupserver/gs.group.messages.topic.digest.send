# coding=utf-8
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.group.messages.senddigest',
    version=version,
    description="The console script for sending the topic digest from "
                "GroupServer.",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='groupserver message post topic digest',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org/',
    license='other',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.group', 'gs.group.messages', ],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'lockfile',
        'gs.form',
        # -*- Extra requirements: -*-
    ],
    entry_points={
        'console_scripts': [
            'senddigest = gs.group.messages.senddigest.script:main',
            ],
        # --=mpj17=-- Entry points are the work of the devil. Some time
        # you, me and Mr Soldering Iron are going to have a little chat
        # about how to do things better.
        },
)
