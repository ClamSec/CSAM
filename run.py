#!flask/bin/python

from app import app

import logging
logging.basicConfig(filename='error.log',level=logging.DEBUG)

app.run(debug=True, host='0.0.0.0',port=5555)
