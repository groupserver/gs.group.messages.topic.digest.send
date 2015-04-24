:mod:`gs.group.topic.digest.send` code
======================================

.. module:: gs.group.messages.topic.digest.send.script

The code for the script that sends out the digest works in two
main stages: first it gets `the list of groups`_, and then it
`sends a digest`_. Both raise the same exceptions.

The list of groups
------------------

The list of groups is retrieved using a web-hook that returns a
list of groups as a JSON blob. The :data:`DIGEST_GROUPS_URI`
specifies the location of the web-hook, relative to the root of
the site, while the :func:`get_digest_groups` function retrieves
the list of groups.

.. autodata:: DIGEST_GROUPS_URI

.. autofunction:: get_digest_groups

.. _sends a digest:

Sending a digest
----------------

The digest is actually send by a web-hook. This hook is located
at :data:`SEND_DIGEST_URI` and is triggered by the
:func:`send_digest` function.

.. autodata:: SEND_DIGEST_URI

.. autofunction:: send_digest


Exceptions
----------

.. autoclass:: NotOk


..  LocalWords:  JSON URI autodata autofunction
