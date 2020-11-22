import logging
import os
from pymongo import MongoClient

from flask import Flask, request

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)

app = Flask(__name__)

FIELDS = ['item', 'qty', 'status', 'size', 'tags']

URI = "mongodb://%s:%s@%s" % ('root', 'example', 'mongo')

@app.route('/index', methods=['GET'])
def index_get():
    """
    Update the Google Drive holding summer pool applicants.

    """
    client = MongoClient(URI)
    db = client.examples
    return {'result': [
        {field: item[field] for field in FIELDS}
        for item in db.inventory.find({})
    ]}
