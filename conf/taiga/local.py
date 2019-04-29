# If you want to modify this file, I recommend check out docker-taiga-example
# https://github.com/benhutchins/docker-taiga-example
#
# Please modify this file as needed, see the local.py.example for details:
# https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example
#
# Importing docker provides common settings, see:
# https://github.com/benhutchins/docker-taiga/blob/master/docker-settings.py
# https://github.com/taigaio/taiga-back/blob/master/settings/common.py

from .docker import *

PUBLIC_REGISTER_ENABLED = False
DEBUG = False
TEMPLATE_DEBUG = False
TAIGA_HOSTNAME=pista.atdsdop.com
TAIGA_SSL_BY_REVERSE_PROXY=true
# TAIGA_SSL=True (see Enabling HTTPS below)
TAIGA_SECRET_KEY=oCy7cWMjESJYesKPaitUETYU7ZfsCodz2UpcWiiytoPY6wFZYXhFHDrynr3bHo
# TAIGA_SKIP_DB_CHECK (set to skip the database check that attempts to automatically setup initial database)
TAIGA_ENABLE_EMAIL=true
TAIGA_EMAIL_FROM=web@atdsdop.com
TAIGA_EMAIL_USE_TLS=true
TAIGA_EMAIL_HOST=box.cincoeuzebio.com
TAIGA_EMAIL_PORT=587
TAIGA_EMAIL_USER=web@atdsdop.com
TAIGA_EMAIL_PASS='4dm1n4TD'