=======================================
``gs.group.messages.topic.digest.send``
=======================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The ``senddigest`` script for GroupServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2015-02-24
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

Introduction
============

This product provides the ``senddigest`` script_ is used to
instruct GroupServer to send a topics digest [#digest]_. This
script is designed to be called on a regular schedule, by a
system such as ``cron``.

Script
======

Usually senddigest is called by ``cron(8)`` once a day to send
the topic digests from GroupServer.

Usage
-----

::

   senddigest [-h] [-c CONFIG] [-i INSTANCE] [-v] url


Positional Arguments
--------------------

``url``:
  The URL for the GroupServer site.

Optional Arguments
------------------

``-h``, ``--help``:
  Show this help message and exit

``-c CONFIG``, ``--config CONFIG``:
  The name of the GroupServer configuration file (default
  ``$INSTANCE_HOME/etc/gsconfig.ini``) that contains the token
  that will be used to authenticate the script when it tries to
  send the digests.

``-i INSTANCE``, ``--instance INSTANCE``:
  The identifier of the GroupServer instance configuration to use
  (default "default").

``-v``, ``--verbose``:
  Provide verbose output. The default is to provide no output (no
  news is good news).

Returns
-------

The script returns ``0`` on success, or non-zero on error. In the
case of an error, ``senddigest`` follows the convention specified
in ``/usr/include/sysexits.h``.

.. [#digest] See `the topics digest egg`_ for more information.
.. _the topics digest egg: https://source.iopen.net/groupserver/gs.group.messages.topicsdigest/summary

- Code repository:
  https://github.com/groupserver/gs.group.messages.digest.send
- Questions and comments to http://groupserver.org/groups/develop
- Report bugs at https://redmine.iopen.net/projects/groupserver

..  LocalWords:  senddigest
