import flask, json, logging
from flask import request, jsonify
from keyvalueapi import KeyValueApi


app = flask.Flask(__name__)
app.config["DEBUG"] = True
logging.basicConfig(level=logging.DEBUG)   
kv = KeyValueApi() 
        

#HomePage
@app.route('/home', methods=['GET'])
def home():
    return jsonify(kv.homepage())

#Metod to set key value 
@app.route('/set', methods=['POST'])
def set_values_to_kv_store():
    try:
        data = json.loads(request.data)
        return kv.set_items(data['key'], data['value'])
    except Exception as error:
        logging.error(error)
        logging.error("Data Couldn't be added to the DB, Please check the above exception")
    

#Method to get a value against a key 
@app.route('/get', methods=['GET'])
def get_all_data_from_database():
    try:
        key = request.args.get('key')
        return jsonify(kv.get_key_value(key))
    except Exception as error:
        logging.error(error)

#Method to search for any key with prefix/suffix
@app.route('/search', methods=['GET'])
def search_for_db_entries():
    try:
        
        if 'prefix' in request.args:
            param = request.args['prefix'] 
            return jsonify(kv.search_prefix_in_key(param))   
        elif 'suffix' in request.args:
            param = request.args['suffix']   
            return jsonify(kv.search_suffix_in_key(param))
    except Exception as error:
        logging.error(error)

app.run()