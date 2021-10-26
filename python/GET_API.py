from flask_cors import CORS
import flask
import csv
from flask import jsonify
import mysql.connector

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

#De inloggegevens van de database staan in een apart document in de volgende vorm: 'user','password','host','naam van de database'

with open(r"C:\Users\caspe\OneDrive\Documents\GitHub\Ontime\ontime\txt\mysql.txt") as f1:
        data=csv.reader(f1,delimiter=",")
        for row in data:
            user=row[0]
            password=row[1]
            host=row[2]
            database=row[3]


@ app.route("/client", methods = ["GET"])
def get_table_detail():
    connection = ontimedb()
    cursor = connection.cursor()
    cursor.execute("""SELECT *
    FROM client""")
    
    results = cursor.fetchall()
    return jsonify(results), 200

def ontimedb():
    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database)

if __name__ == "__main__":
    app.run(debug=True)