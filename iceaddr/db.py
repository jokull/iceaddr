# -*- encoding: utf-8 -*-
"""

    iceaddr: Look up information about Icelandic street addresses and postcodes
    Copyright (c) 2018 Sveinbjorn Thordarson

"""

from __future__ import unicode_literals

import sqlite3
import pkg_resources

class SharedDB():
    
    def __init__(self):
        self.db_conn = None
    
    def connection(self):
        # Open connection lazily
        if not self.db_conn:
            db_path = pkg_resources.resource_filename(__name__, 'resources/stadfangaskra.db')
            self.db_conn = sqlite3.connect(db_path)
            self.db_conn.row_factory = lambda c, r: dict(zip([col[0] for col in c.description], r))
            
        return self.db_conn

shared_db = SharedDB()