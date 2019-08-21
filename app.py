#!usr/bin/python3
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)

medition_type = { 'sensor': 'FC28', 'variable': 'humidity', 'units': '%water by ground volume' } #KWArgw = keywords

meditions = [
    { 'date': '2019-08-10 01:24:08', **medition_type, 'value': 10 },
    { 'date': '2019-08-10 02:24:08', **medition_type, 'value': 11 },
    { 'date': '2019-08-10 03:24:08', **medition_type, 'value': 12 },
    { 'date': '2019-08-10 04:24:08', **medition_type, 'value': 13 },
    { 'date': '2019-08-10 05:24:08', **medition_type, 'value': 14 },
    { 'date': '2019-08-10 06:24:08', **medition_type, 'value': 14 },
    { 'date': '2019-08-10 07:24:08', **medition_type, 'value': 13 },
    { 'date': '2019-08-10 08:24:08', **medition_type, 'value': 12 },
    { 'date': '2019-08-10 09:24:08', **medition_type, 'value': 11 },
    { 'date': '2019-08-10 09:24:08', **medition_type, 'value': 9 }
]

#-------------------------------- GET ROUTES -----------------------------#

@app.route('/')
def get():
    return jsonify(medition_type)


@app.route('/getAllMeditions')
#This GET route returns all meditions in memory
def getAll():
    return jsonify(meditions)


@app.route('/getMediana')
def mediana():
    #Gets the ordered list of values 
    values = []
    for medition in meditions:
        if medition['value'] not in values:
            values.append(medition['value'])
    values.sort()
    #Get mediana
    mediana = values[int(len(values)/2)]
    if len(values)%2 != 0:
        return jsonify({ "mediana": mediana })
    mediana = (mediana + values[(int(len(values)/2)-1)])/2
    return jsonify({ "mediana": mediana })
    
#------------------------------------------- POST ROUTES -----------------------------------

# GET is the default method
@app.route('/add_medition', methods = ['POST']) 
def post_medition():
    body = request.json
    date = datetime.strftime(datetime.now(), '%y-%m-%d %H:%M:%S')
    medition = { "date": date, **medition_type, "value": body['value'] }
    meditions.append(medition)
    return jsonify(medition)

#------------------------------------------- DELETE ROUTES ---------------------------------

@app.route('/deleteAll', methods = ['DELETE'])
def deleteAll():
    meditions = []
    return jsonify(meditions)

if __name__ == '__main__':
    app.run(port = 3000, debug = True)


#
#@app.route('/meditions/date/<string:date>', methods = ['GET'])
#def getByDate(date):
#    x = None
#    for meditions 
#
