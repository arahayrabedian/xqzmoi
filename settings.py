import os

from bottle import TEMPLATE_PATH


DATABASE_CONNECTION_STRING = os.getenv("XQZES_DATABASE_CONNECTION_STRING",
                                       "sqlite:///excuses.sqlite")

SLACK_OAUTH = {
    'client_id': os.getenv('SLACK_OAUTH_CLIENT_ID', None),
    'client_secret': os.getenv('SLACK_OAUTH_CLIENT_SECRET', None),
    'token_url': 'https://slack.com/api/oauth.access',
    'command_scope': 'commands',
}

#  modify template path for production
_TEMPLATE_PATH = os.getenv('XQZES_BOTTLE_TEMPLATE_PATH', './templates/')
TEMPLATE_PATH.insert(0, _TEMPLATE_PATH)