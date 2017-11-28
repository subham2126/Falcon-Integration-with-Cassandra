# things.py

# Let's get this party started!
import falcon
import json
from cassandra.cluster import Cluster
cluster = Cluster(["127.0.0.1"])


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class ThingsResource(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        session = cluster.connect('tutorialspoint')
        rows = session.execute('SELECT emp_id, emp_city, emp_name FROM emp')
        rows_as_dict = []
        for row in rows:
            temp = {
                'id' : row.emp_id,
                'city' : row.emp_city,
                'name' : row.emp_name}
            rows_as_dict.append(temp)
            print (row.emp_id, row.emp_city, row.emp_name)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body =((json.dumps(rows_as_dict)))
    def on_set(self, req, resp):
        """Handles GET requests"""
        session = cluster.connect('tutorialspoint')
        rows = session.execute('SELECT emp_id, emp_city, emp_name FROM emp')
        rows_as_dict = []
        for row in rows:
            temp = {
                'id' : row.emp_id,
                'city' : row.emp_city}
            rows_as_dict.append(temp)
            print (row.emp_id, row.emp_city, row.emp_name)
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body =((json.dumps(rows_as_dict)))

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = ThingsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)
app.add_route('/things2', things)