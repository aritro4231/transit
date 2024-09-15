from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from OSMPythonTools.api import Api
from OSMPythonTools.overpass import Overpass
from OSMPythonTools.overpass import overpassQueryBuilder
from OSMPythonTools.nominatim import Nominatim

app = Flask(__name__)
CORS(app)  # Enable CORS

api = Api()
overpass = Overpass()
nominatim = Nominatim()
client = MongoClient('mongodb+srv://busdatacollection.vhbsy.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority&appName=BusDataCollection')
db = client['busreviews']
reviews_collection = db['reviews']
stops = ["Transit Center Orange #8113", "Transit Center Maroon #8002", "University City/Glade Sbnd #1314", "Gables Shopping Center #1607", "Walmart #1802"]

transitCenterOrange = overpassQueryBuilder(elementType='node', area=nominatim.query('Blacksburg, Virginia'), selector=['"name"~"Orange Loop Bay 13"'])


@app.route('/submit-review', methods=['POST'])
def submitreview():
    review_data = request.json
    reviews_collection.insert_one(review_data)
    return jsonify({'message' : 'Review submitted successfully'}), 200

@app.route('/return-comments', methods=['POST'])    
def returncomments():
    i = 0
    result = {}
    for json in reviews_collection:
        result[i] = {json['account'] : json['comment']}
        i += 1
    return jsonify(result)

@app.route('/return-stops-near-location', methods=['POST'])
def returnstopsnearlocation():
        location = request.args.get('location')
    
if __name__ == '__main':
    app.run(debug=True)