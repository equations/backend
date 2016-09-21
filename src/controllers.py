# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

from .context import *
from .utils import *


def read_context(label, depth=0) -> str:
    """
    Retrieve context by context label.
    """

    session = open_session()
    data = query_context(
        ":Context {{label: '{}'}}".format(label),
        depth,
        session,
        vars_info=True)
    session.close()
    return data


def read_root_context(depth=1) -> str:
    """
    Retrieve root context.
    """

    session = open_session()
    data = query_context(':ContextRoot', depth, session, children_only=True)
    session.close()
    return data


def create_context(body) -> str:
    """
    Create new context (immutable).
    """

    # Read parent and label.
    label = body['label']
    parent = body['parent'] if 'parent' in body else None

    # Check label and parent formatting (lowercase alpha only).
    if is_spinal_case(label) and (
            parent is None or is_spinal_case(parent)):
        parent_query = ":Context {{label: '{}'}}".format(
            parent) if parent is not None else ':ContextRoot'

        # Create new context node.
        return create_record('''
            MATCH (parent{})
            CREATE (node:Context {{label: '{}'}})-[:BelongsTo]->(parent)
            RETURN node
            '''.format(parent_query, label))
    else:
        return {
            'status': 'format-error',
            'message': 'Rejected based on incorrect string formatting.'
        }, 400


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

    # Read label, latex, context, parent, expr
    label = body['label']
    latex = body['latex']
    context = body['context']
    parent = body['parent'] if 'parent' in body else None
    expr = body['expr']

    # TODO: check LaTeX and expression formatting.
    # TODO: check validity of parent variable.
    if is_spinal_case(context) and (parent is None or is_spinal_case(parent)):
        # Create new context node.
        if parent is None:
            return create_record('''
                MATCH (context:Context {{label: '{}'}})
                CREATE (node:Variable {{label: '{}', latex: '{}', expr: '{}'}})-[:BelongsTo]->(context)
                RETURN node
                '''.format(context, label, latex, expr))
        else:
            return create_record('''
                MATCH (context:Context {{label: '{}'}})
                MATCH (parent:Variable {{label: '{}'}})
                CREATE (node:Variable {{label: '{}', latex: '{}', expr: '{}'}})-[:BelongsTo]->(context)
                CREATE (node)-[:Implements]->(parent)
                RETURN node
                '''.format(context, parent, label, latex, expr))
    else:
        return {
            'status': 'format-error',
            'message': 'Rejected based on incorrect string formatting.'
        }, 400


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
