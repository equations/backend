# Copyright (c) 2016, Herman Bergwerf. All rights reserved.
# Use of this source code is governed by an AGPL-3.0-style license
# that can be found in the LICENSE file.

from eqs_backend.eqs_backend import server

if __name__ == "__main__":
    server.run(port=8080)
