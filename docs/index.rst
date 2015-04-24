:mod:`gs.group.messages.topic.digest.send`
==========================================

The :mod:`gs.group.messages.topic.digest.send` product provides
the :program:`senddigest` script. This script is used to send out
the daily digest of topics once a day, and is normally called by
:manpage:`cron(8)`.

The :doc:`code` does only triggers two web-hooks. Both these
hooks are provided by the
:mod:`gs.group.messages.topic.digest.base` product [#base]_.

Contents:

.. toctree::
   :maxdepth: 2

   command
   code
   HISTORY

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.messages.topic.digest.send
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. [#base] See
             <https://github.com/groupserver/gs.group.messages.topic.digest.base>
