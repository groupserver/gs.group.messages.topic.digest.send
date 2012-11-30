Introduction
============

This product provides the ``senddigest`` script_ is used to instruct
GroupServer to send a topics digest [#digest]_. This script is designed to
be called on a regular schedule, by a system such as ``cron``.

Script
======

Usually senddigest is called by cron(8) once a day to send the topic
digests from GroupServer.

Usage
-----

::

   senddigest [-h] [-c CONFIG] [-i INSTANCE] url


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
  ``$INSTANCE_HOME/etc/gsconfig.ini``) that contains the token that will be
  used to authenticate the script when it tries to send the digests.

``-i INSTANCE``, ``--instance INSTANCE``
  The identifier of the GroupServer instance configuration to use (default
  "default").

Returns
-------

The script returns ``0`` on success, or non-zero on error. In the case of
an error, ``senddigest`` follows the convention specified in
``/usr/include/sysexits.h``.

.. [#digest] See `the topics digest egg`_ for more information.
.. _the topics digest egg: https://source.iopen.net/groupserver/gs.group.messages.topicsdigest/summary

- Code repository:
  https://source.iopen.net/groupserver/gs.group.messages.senddigest
- Questions and comments to http://groupserver.org/groups/develop
- Report bugs at https://redmine.iopen.net/projects/groupserver
