# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

from .dbutils import *


def read_context(label, depth=1) -> str:
    """
    Retrieve context by context label.
    """

    return '{}'


def read_root_context(depth=1) -> str:
    """
    Retrieve root context.
    """

    return '{}'


def create_context(body) -> str:
    """
    Create new context (immutable).
    """

    return '{}'


def find_variables(q) -> str:
    """
    Find variables using SymPy expression query.
    """

    return '[]'


def read_variable(label) -> str:
    """
    Retrieve variable by label.
    """

    return '{}'


def create_variable(body) -> str:
    """
    Create new variable (immutable).
    """

    return '{}'


def find_derivations(q) -> str:
    """
    Find derivations using SymPy expression query.
    """

    return '[]'


def create_derivation(body) -> str:
    """
    Create new derivation (immutable).

    A derivation has the following structure:
    - One source relation: the derivation loads an external equation as base,
      the source can be either a variable definition or another derivation.
    - A number of substitutions: other expressions can be substituted including
      variable definitions and other derivations.
    - Rewritten expression: the expression that is equal to the source equation
      after all substitutions are applied.

    A derivation does not neccesarily have to substitute other equations. It can
    simply be a rewritten form of the source equation. Note that SymPy can also
    find simple derivations.
    """

    return '{}'
