:program:`senddigest`
=====================

.. program:: senddigest

Synopsis
--------

   :program:`senddigest` [:option:`-h`] [:option:`-c` <CONFIG>] [:option:`-i` <INSTANCE>] [:option:`-v`] :option:`url`

Description
-----------

Usually :program:`senddigest` is called by :manpage:`cron(8)`
once a day to send the *daily digest of topics* from GroupServer
to all the members of all the groups whose email settings are set
to *digest*.

Positional arguments
--------------------

.. option:: url

  The URL for the GroupServer site.

Optional arguments
------------------

.. option:: -h, --help

  Show this help message and exit

.. option:: -c <CONFIG>, --config <CONFIG>

  The name of the GroupServer configuration file (default
  :file:`{INSTANCE_HOME}/etc/gsconfig.ini`) that contains the
  token that will be used to authenticate the script when it
  tries to send the digests.

.. option:: -i <INSTANCE>, --instance <INSTANCE>

  The identifier of the GroupServer instance configuration to use
  (default ``default``).

.. option:: -v, --verbose

  Provide verbose output. The default is to provide no output (no
  news is good news).

Returns
-------

The script returns ``0`` on success, or non-zero on error. In the
case of an error, :program:`senddigest` follows the convention specified
in :file:`/usr/include/sysexits.h`.
