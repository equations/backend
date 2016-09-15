# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

import json


def isDictAndContains(data, keys):
    if isinstance(data, dict):
        for key in keys:
            if key not in data:
                return False
        return True
    else:
        return False


def dumpMessage(status, message=''):
    return json.dumps({
        'status': status,
        'message': message
    })
