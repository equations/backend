# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

import re


def resolve_variables(expr) -> list:
    """
    Function to find all variables in a SymPy expression. This function assumes
    all non variables are followed by an opening parenthesis, this might not
    always be the case.

    Notes:
    - This approach collides with built-in symbols like pi and E.
    """

    rmfns = re.compile(r'[A-z]+\(')
    fvars = re.compile(r'[A-z]+')
    expr = rmfns.sub('(', expr)
    matches = fvars.findall(expr)

    allvars = []
    for match in matches:
        variable = match.group(1)
        if variable not in allvars:
            allvars.append(variable)

    return allvars
