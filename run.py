# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

import connexion
import src

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./doc/')
    app.add_api(
        'swagger.yaml',
        strict_validation=True,
        arguments={
            'title': 'The Equation Database API'})
    app.run(port=8080)
