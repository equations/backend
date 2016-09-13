# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

from flask import Flask, request
from neo4j.v1 import GraphDatabase, basic_auth
import json

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


@server.route('/derive/', methods=['POST'])
def appendDerivation():
    """
    Append derivation to exiting equation.
    """

    return '{}'


@server.route('/definition/', methods=['POST'])
def addDefinition():
    """
    Add new definition within the given context.
    """

    return '{}'


@server.route('/context/', methods=['POST'])
def appendContext():
    """
    Append context to the given parent context.
    If no parent is defined the context is appended to the context root.
    """

    data = request.get_json()
    if isinstance(data, dict) and 'label' in data:
        db = openDb()

        # Find parent query.
        parent = "Context {label:'%s'}" % data[
            'parent'] if 'parent' in data else 'ContextRoot'

        # Run query.
        db.run('''
        MATCH (parent:%s)
        CREATE (node:Context {label:'%s'})
        CREATE (node)-[:BelongsTo]->(parent)
        ''' % (parent, data['label']))

        db.close()

        return json.dumps({
            'status': 'processed'
        })
    else:
        return json.dumps({
            'status': 'failed',
            'message': 'No context label provided.'
        })
