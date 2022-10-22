import logging
import os
from pymongo import MongoClient

from flask import Flask
#from flask.ext.sentinel import ResourceOwnerPasswordCredentials, oauth

logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)

app = Flask(__name__)

FIELDS = ['item', 'qty', 'status', 'size', 'tags']

URI = "mongodb://%s:%s@%s" % ('root', 'example', 'mongo')

@app.route('/index', methods=['GET'])
@oauth.require_oauth()
def index_get():
    """
    Update the Google Drive holding summer pool applicants.

    """
    client = MongoClient(URI)
    # examples is the DB
    db = client.examples
    return {'result': [
        {field: item[field] for field in FIELDS}
        # inventory is the collection
        for item in db.inventory.find({})
    ]}

if __name__ == '__main__':
    print("if __name__ == '__main__':")
    ResourceOwnerPasswordCredentials(app)
    app.run(ssl_context='adhoc')
