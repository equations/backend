# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

from enum import Enum


class ExprRefType(Enum):
    variable = 1
    derivation = 2


class ExprRef:
    reftype = None
    refid = None
