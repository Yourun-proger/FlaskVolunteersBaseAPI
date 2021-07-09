from flask import Flask, jsonify, request
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
@app.route("/districts")
def get_districts():
    districts = json.loads(open('districts.json', 'r', encoding='utf-8').read())
    return jsonify(districts)
@app.route('/streets')
def get_streets():
    district_id = request.args.get('district')
    streets = json.loads(open('streets.json', 'r', encoding='utf-8').read())
    districts = json.loads(open('districts.json', 'r', encoding='utf-8').read())
    if district_id is None:
        return jsonify(streets)
    else:
        try:
            streets_sort = []
            cur_district = districts[district_id]
            for street_id in cur_district['streets']:
                streets_sort.append({
                        **{'id': str(street_id)},
                        **streets[str(street_id)]
                    })
            return jsonify(streets_sort)
        except KeyError:
            return jsonify(), 400
@app.route('/volunteers')
def get_volunteers():
    street_id = request.args.get('streets')
    volunteers = json.loads(open('volunteers.json', 'r', encoding='utf-8').read())
    streets = json.loads(open('streets.json', 'r', encoding='utf-8').read())
    if street_id is None:
        return jsonify(volunteers)
    else:
        try:
            volunteers_sort = []
            cur_street = streets[street_id]
            for volunteer_id in cur_street['volunteer']:
                volunteers_sort.append({
                    **{'id': int(volunteer_id)},
                    **volunteers[str(volunteer_id)]
                    })
            return jsonify(volunteers_sort)
        except KeyError:
            return jsonify(), 400
@app.route('/helpme', methods=['POST'])
def post_help_request():
    if request.method == 'POST':
        data = request.json
        return jsonify({'status': 'succes'}), 201
app.run()
