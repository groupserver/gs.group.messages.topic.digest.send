# -*- coding: utf-8 -*-
############################################################################
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
############################################################################
# Standard libraries
from __future__ import absolute_import, unicode_literals, print_function
from argparse import ArgumentParser  # Standard in Python 2.7
from httplib import OK as HTTP_OK
from json import loads as load_json
from operator import itemgetter
import sys
from urlparse import urlparse
# GroupServer libraries
from gs.config.config import Config, ConfigError
from gs.form import post_multipart
# Local libraries
from .errorvals import exit_vals


class NotOk(Exception):
    pass


def get_args(configFileName):
    p = ArgumentParser(
        description='Send the topic digests from GroupServer.',
        epilog='Usually %(prog)s is called by cron(8) once a day.')
    p.add_argument('url', metavar='url',
                   help='The URL for the GroupServer site.')
    p.add_argument(
        '-c', '--config', dest='config', default=configFileName, type=str,
        help='The name of the GroupServer configuration file (default '
             '"%(default)s") that contains the token that will be used to '
             'authenticate the script when it tries to send the digests.')
    p.add_argument(
        '-i', '--instance', dest='instance', default='default', type=str,
        help='The identifier of the GroupServer instance configuration to '
             'use (default "%(default)s").')
    p.add_argument(
        '-v', '--verbose', dest='verbose', default=False,
        action='store_true',
        help='Turn on verbose output (feedback). Default %(default)s.')
    retval = p.parse_args()
    return retval


def get_token_from_config(configSet, configFileName):
    config = Config(configSet, configFileName)
    config.set_schema('webservice', {'token': str})
    ws = config.get('webservice')
    retval = ws['token']
    if not retval:
        m = 'The token was not set.'
        raise ValueError(m)
    return retval


DIGEST_GROUPS_URI = '/gs-group-messages-topic-digest-groups.html'


def get_digest_groups(hostname, token):
    'Get the list of groups to send the digest to.'
    fields = {'token': token, 'get': '', }
    status, reason, data = post_multipart(hostname, DIGEST_GROUPS_URI,
                                          fields)  # port?
    if status != HTTP_OK:
        m = '{reason} ({status} <{host}>)'
        msg = m.format(reason=reason, status=status, host=hostname)
        raise NotOk(msg)

    retval = load_json(data)
    retval.sort(key=itemgetter(0, 1))  # Nicer when sorted by site & group
    return retval


SEND_DIGEST_URI = '/gs-group-messages-topic-digest-send.html'


def send_digest(hostname, siteId, groupId, token):
    fields = {
        'form.siteId': siteId,
        'form.groupId': groupId,
        'form.token': token,
        'form.actions.send': 'Send'}
    status, reason, data = post_multipart(hostname, SEND_DIGEST_URI,
                                          fields)  # port?
    if status != HTTP_OK:
        m = '{reason} ({status} <{host}>)'
        msg = m.format(reason=reason, status=status, host=hostname)
        raise NotOk(msg)


def main(configFileName='etc/gsconfig.ini'):
    args = get_args(configFileName)
    try:
        token = get_token_from_config(args.instance, args.config)
    except ConfigError as ce:
        m = 'Error with the configuration file "{config}":\n{error}\n'
        msg = m.format(config=args.config, error=ce.message)
        sys.stderr.write(msg)
        sys.exit(exit_vals['config_error'])

    parsedUrl = urlparse(args.url)
    if not parsedUrl.hostname:
        m = 'No host in the URL <{0}>\n'.format(args.url)
        sys.stderr.write(m)
        sys.exit(exit_vals['url_bung'])
    hostname = parsedUrl.hostname

    if args.verbose:
        sys.stdout.write('Retrieving the list of groups\n')
    try:
        groups = get_digest_groups(hostname, token)
    except NotOk as no:
        m = 'Error communicating with the server while recieving the '\
            'list of groups to send the digest to:\n{message}\n'
        msg = m.format(message=no)
        sys.stderr.write(msg)
        sys.exit(exit_vals['communication_failure'])

    m = 'Sending digest to {0} on {1}\n'
    for siteId, groupId in groups:
        if args.verbose:
            sys.stdout.write(m.format(groupId, siteId))
        try:
            send_digest(hostname, siteId, groupId, token)
        except NotOk, no:
            m = 'Error communicating with the server while sending the '\
                'digest to the group {0} on the site {1}:\n{2}\n'
            msg = m.format(siteId, groupId, no)
            sys.stderr.write(msg)

    sys.exit(exit_vals['success'])

if __name__ == '__main__':
    main()
