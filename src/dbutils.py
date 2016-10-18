# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

import os
from neo4j.v1 import GraphDatabase, basic_auth
from py2neo import Graph, authenticate

driver = GraphDatabase.driver(
    'bolt://0.0.0.0',
    auth=basic_auth(
        os.getenv('EQS_NEO4J_USER'),
        'dev'))

# print(os.getenv('EQS_NEO4J_PASS'))
'''
# authenticate(
#    "0.0.0.0:7474",
#    os.getenv('EQS_NEO4J_USER'),
#    os.getenv('EQS_NEO4J_PASS'))
graph = Graph(bolt=True, host='0.0.0.0', user=os.getenv('EQS_NEO4J_USER'),
              password='neo4j')
print(graph.data("MATCH (a:Context) RETURN a.label"))
'''


def init_db():
    """
    Setup database constraints.
    """

    session = open_session()
    session.run('''
CREATE (:ContextRoot)
CREATE INDEX ON :Context(label)
CREATE INDEX ON :Variable(label)
CREATE INDEX ON :Variable(expr)
CREATE INDEX ON :Derivation(lhs)
CREATE INDEX ON :Derivation(rhs)
CREATE CONSTRAINT ON (node:Context) ASSERT node.label IS UNIQUE
CREATE CONSTRAINT ON (node:Variable) ASSERT node.label IS UNIQUE
''')
    session.close()


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
