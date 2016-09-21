# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

import re

spinal_case_re = re.compile('[a-z-]+')


def is_spinal_case(string):
    return spinal_case_re.match(string) is not None
