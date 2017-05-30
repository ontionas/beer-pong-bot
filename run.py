#!/usr/bin/python

import sys
import os
import json

import bpbot.bpbot as bp

if len(sys.argv) is 2: #config file is specified
    config_file = os.path.normpath(sys.argv[1])
else:
    config_file = os.path.join('.', 'data', 'config.json')

with open(config_file) as data_file:
    config = json.load(data_file)

bp.initialize(
    bot_id=config['bot_id'],
    debug=config['debug'],
    manual_push=config['manual_push'],
    use_spreadsheet=config['use_spreadsheet'],
    google_credentials_filename=config['google_credentials_filename']
    )
bp.listen(port=config['listening_port']) #blocking call
