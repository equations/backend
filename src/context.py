# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

from .dbutils import *


def add_to_context_tree(tree, nodes):
    for node in nodes:
        props = node.properties
        label = props['label']
        tree[label] = tree[label] if label in tree else {}
        tree[label]['id'] = node.id
        tree[label]['children'] = {}
        tree = tree[label]['children']


def unwrap_context_tree(tree):
    children = []
    for key, value in tree.items():
        children.append({
            'id': value['id'],
            'label': key,
            'children': unwrap_context_tree(value['children'])
        })
    return children


def query_context(query, depth, session, children_only=False, vars_info=False):
    print(query)
    result = session.run('''
        MATCH path = ({})<-[:BelongsTo*0..{}]-(:Context)
        RETURN path
        '''.format(query, depth))

    root = None
    tree = {}

    # Create context tree.
    for record in result:
        path = record.values()[0]

        # Store root node.
        if root is None and len(path.nodes) > 0:
            root = path.nodes[0]

        add_to_context_tree(tree, path.nodes[1:])

    # Convert tree to nested arrays.
    children = unwrap_context_tree(tree)

    if root is None:
        return {
            'status': 'notfound',
            'message': 'Request context root could not be found.'
        }, 404

    if children_only:
        return children
    else:
        data = {
            'id': root.id,
            'label': root.properties['label'],
            'children': children
        }

        # Add information about variables.
        # if vars_info:
        #     ...

        return data
