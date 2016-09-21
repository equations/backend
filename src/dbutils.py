# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

import os
from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
    'bolt://0.0.0.0',
    auth=basic_auth(
        os.getenv('EQS_NEO4J_USER'),
        os.getenv('EQS_NEO4J_PASS')))


def setup_db_constraints():
    """
    Setup database constraints.
    """

    db.run('''
CREATE (:ContextRoot)
CREATE INDEX ON :Context(label)
CREATE INDEX ON :Variable(label)
CREATE INDEX ON :Variable(expr)
CREATE INDEX ON :Derivation(lhs)
CREATE INDEX ON :Derivation(rhs)
CREATE CONSTRAINT ON (node:Context) ASSERT node.label IS UNIQUE
CREATE CONSTRAINT ON (node:Variable) ASSERT node.label IS UNIQUE
''')


def open_session():
    """
    Open Neo4j session.
    """

    return driver.session()


def create_record(query):
    session = open_session()
    result = session.run(query)
    record = result.single().values()[0]
    data = record.properties
    data['id'] = record.id
    session.close()
    return data
