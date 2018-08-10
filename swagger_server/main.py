#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import connexion
import sys
import os


path = os.path.realpath(__file__)
path1 = os.path.dirname(path)
path2= os.path.dirname(path1)

sys.path.append(path2)

for path in sys.path:
    print(path)


from swagger_server import encoder


app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'TransitServer'})
# app.run(port=8080)
