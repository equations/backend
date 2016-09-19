# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.


def read_context(label, depth=1) -> str:
    """
    Retrieve context by context label.
    """

    return 'do some magic!'


def read_root_context(depth=1) -> str:
    """
    Retrieve root context.
    """

    return 'do some magic!'


def create_context(body) -> str:
    """
    Create new context (immutable).
    """

    return 'do some magic!'


def find_variables(q) -> str:
    """
    Find variables using SymPy expression query.
    """

    return 'do some magic!'


def read_variable(label) -> str:
    """
    Retrieve variable by label.
    """

    return 'do some magic!'


def create_variable(body) -> str:
    """
    Create new variable (immutable).
    """

    return 'do some magic!'


def find_derivations(q) -> str:
    """
    Find derivations using SymPy expression query.
    """

    return 'do some magic!'


def create_derivation(body) -> str:
    """
    Create new derivation (immutable).
    """

    return 'do some magic!'
