# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import logging
from sys import argv

from uniborg import Uniborg
import config

logging.basicConfig(level=logging.INFO)
try:
    session_name = argv[1]
except IndexError:
    session_name = "stdbot"


borg = Uniborg(
    session_name,
    plugin_path="botplugins",
    admins=config.admins,
    connection_retries=None,
    api_id=config.id,
    api_hash=config.hash
)

borg.run_until_disconnected()
