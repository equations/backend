#!/bin/bash

# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

# Export Neo4j credentials.
source dev.conf

# Run server.
sudo -E python3 run.py
