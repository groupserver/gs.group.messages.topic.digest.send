# -*- coding: utf-8 -*-
# Standard libraries
from argparse import ArgumentParser  # Standard in Python 2.7
from httplib import OK as HTTP_OK
import sys
from urlparse import urlparse
# GroupServer libraries
from gs.config.config import Config, ConfigError
from gs.form import post_multipart
# Local libraries
from errorvals import exit_vals


class NotOk(Exception):
    pass


def get_args(configFileName):
    p = ArgumentParser(description='Send the topic digests from GroupServer.',
                       epilog='Usually %(prog)s is called by cron(8) once a '
                           'day.')
    p.add_argument('url', metavar='url',
                   help='The URL for the GroupServer site.')
    p.add_argument('-c', '--config', dest='config', default=configFileName,
                   type=str,
                   help='The name of the GroupServer configuration file '
                       '(default "%(default)s") that contains the token that '
                       'will be used to authenticate the script when it tries '
                       'to send the digests.')
    p.add_argument('-i', '--instance', dest='instance', default='default',
                   type=str,
                   help='The identifier of the GroupServer instance '
                       'configuration to use (default "%(default)s").')
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


SEND_DIGEST_URI = '/gs-group-messages-topicsdigest-send.html'


def send_digest(url, token):
    parsedUrl = urlparse(url)
    if not parsedUrl.hostname:
        m = 'No host in the URL <{0}>\n'.format(url)
        sys.stderr.write(m)
        sys.exit(exit_vals['url_bung'])
    hostname = parsedUrl.hostname
    fields = {'form.actions.send': 'Send'}
    status, reason, data = post_multipart(hostname, SEND_DIGEST_URI,
                                          fields)  # port?
    if status != HTTP_OK:
        m = '{reason} ({status} <{host}>)'.format(reason=reason, status=status,
                                                    host=hostname)
        raise NotOk(m)


def main(configFileName):
    args = get_args(configFileName)
    try:
        token = get_token_from_config(args.instance, args.config)
    except ConfigError, ce:
        m = 'Error with the configuration file "{config}":\n{error}\n'
        msg = m.format(config=args.config, error=ce.message)
        sys.stderr.write(msg)
        sys.exit(exit_vals['config_error'])

    try:
        send_digest(args.url, token)
    except NotOk, no:
        m = 'Error communicating with the server while sending the digests:'\
            '\n{message}\n'
        msg = m.format(message=no)
        sys.stderr.write(msg)
        sys.exit(exit_vals['communication_failure'])

    sys.exit(exit_vals['success'])

if __name__ == '__main__':
    main('etc/gsconfig.ini')
