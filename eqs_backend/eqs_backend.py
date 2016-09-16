# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

from flask import Flask, request
from neo4j.v1 import GraphDatabase, basic_auth
from .helpers import *


# Define Flask server instance.
server = Flask(__name__)
driver = GraphDatabase.driver(
    'bolt://0.0.0.0',
    auth=basic_auth(
        'neo4j',
        'test'))


def setupDb():
    """
    Setup empty database.
    """

    db.run('CREATE (:ContextRoot)')
    db.run('CREATE CONSTRAINT ON (node:Context) ASSERT node.label IS UNIQUE')
    db.run('CREATE CONSTRAINT ON (node:Variable) ASSERT node.label IS UNIQUE')


def openDb():
    """
    Open Neo4j session.
    """

    return driver.session()


@server.route('/equation/', methods=['GET'])
def listEquations():
    """
    REST interface for retrieving equations.
    """

    return '{}'


@server.route('/search/')
def textSearch():
    """
    Fulltext search interface to search for:
    - contexts
    - equation labels
    - variables and aliases
    """

    return '{}'


@server.route('/derivation/', methods=['POST'])
def appendDerivation():
    """
    # Add derivation

    A derivation has the following structure:
    - One source relation: the derivation loads an external equation as base,
      the source can be either a variable defenition or another derivation.
    - A number of substitutions: in the derivation other equations or variable
      definitions can be used for substitution.
    - Rewritten expression: the expression that is equal to the source equation
      after all substitutions are applied.

    A derivation does not neccesarily have to substitute other equations. It can
    simply be a rewritten form of the source equation. Note that SymPy can
    assist in creating derivations. The main point is providing a more flexible
    environment for adding custom derivations, and controlling which steps are
    shown to the user.
    """

    data = request.get_json()
    if isDictAndContains(data, ['source', 'subs', 'expr']):
        db = openDb()

        # Retrieve source equation.

        # Execute substitutions.

        # Check output expression.

        # Write expression to database.

        db.close()

        return dumpMessage('processed')
    else:
        return dumpMessage('failed', 'Incomplete data.')


@server.route('/variable/', methods=['POST'])
def addVariable():
    """
    Add new variable within the given context.
    """

    data = request.get_json()
    if isDictAndContains(data, ['label', 'latex', 'parent', 'expr']):
        db = openDb()

        # Run query.
        db.run('''
        MATCH (parent:Context {{label:'{}'}})
        CREATE (node:Variable {{label:'{}', latex:'{}', expr:'{}'}})
        CREATE (node)-[:BelongsTo]->(parent)
        '''.format(data['parent'], data['label'], data['latex'], data['expr']))

        db.close()

        return dumpMessage('processed')
    else:
        return dumpMessage('failed', 'Incomplete data.')


@server.route('/context/', methods=['POST'])
def appendContext():
    """
    Append context to the given parent context.
    If no parent is defined the context is appended to the root context.
    """

    data = request.get_json()
    if isDictAndContains(data, ['label']):
        db = openDb()

        # Find parent query.
        parent = "Context {label:'{}'}".format(data[
            'parent']) if 'parent' in data else 'ContextRoot'

        # Run query.
        db.run('''
        MATCH (parent:{})
        CREATE (node:Context {{label:'{}'}})
        CREATE (node)-[:BelongsTo]->(parent)
        '''.format(parent, data['label']))

        db.close()

        return dumpMessage('processed')
    else:
        return dumpMessage('failed', 'No context label provided.')
