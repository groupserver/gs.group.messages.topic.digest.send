# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import os
import sys
from setuptools import setup, find_packages
from version import get_version

version = get_version()

# The argparse library was added to core in Python 2.7
core = ['setuptools',
        'gs.config',  # Note: without zope-support
        'gs.form', ]
if sys.version_info > (2, 6):
    requires = core
else:
    requires = core + ['argparse']

setup(name='gs.group.messages.senddigest',
    version=version,
    description="The console script for sending the topic digest from "
                "GroupServer.",
    long_description=open("README.rst").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.rst")).read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: Zope Public License',
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux"
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='groupserver message post topic digest script command send',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org/',
    license='ZPL 2.1',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs', 'gs.group', 'gs.group.messages', ],
    include_package_data=True,
    zip_safe=True,  # --=mpj17=-- Actually zip_safe
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'senddigest = gs.group.messages.senddigest.script:main',
            ],
        # --=mpj17=-- Entry points are the work of the devil. Some time
        # you, me and Mr Soldering Iron are going to have a little chat
        # about how to do things better.
        },
)
