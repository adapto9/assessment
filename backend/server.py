from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from database import DatabaseUtil
from util import Util

import csv
import codecs

######################################################
# Globals

app = Flask(__name__, static_folder='static')
CORS(app)
inUse = False

######################################################
# Routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods = ['GET'])
def getUsers():
    try:
        # Init
        db = DatabaseUtil()
        util = Util()
        
        # Validation for request params
        minSal = request.args.get('minSalary', type=float)
        maxSal = request.args.get('maxSalary', type=float)
        offset = request.args.get('offset', type=int)
        limit = request.args.get('limit', type=int)
        sort = request.args.get('sort', type=str)
        if not util.isValidParams(minSal, maxSal, offset, limit, sort):
            return jsonify({ 'results': 'Invalid parameters' }), 400
        else:
            # Prepare params
            params, sorting = util.prepareParams(minSal, maxSal, offset, limit, sort)
            
            # Query DB to get employees
            count = db.getEmployeeDashboardCount(params, sorting)
            res = db.getEmployeeDashboard(params, sorting)
            
            # Format the json response
            for i in range(len(res)):
                res[i] = { 'id': res[i][0], 'login': res[i][1], 'name': res[i][2], 'salary': res[i][3] }
            return jsonify({ 'results': res, 'count': count }), 200
    except Exception as e:
        print(e)
        return jsonify({ 'results': 'Exception ocurred' }), 500
    finally:
        db.close()


@app.route('/users/upload', methods = ['POST'])
def upload():
    global inUse
    if inUse:
        return jsonify({ 'results': 'Rejected as another file is currently being uploaded' }), 503
    try:
        # Init
        db = DatabaseUtil()
        util = Util()
        inUse = True
        rejected = False
        rejectedReason = ''

        # Check if file exists
        uploaded = request.files['file']
        if not uploaded:
            rejected = True
            rejectedReason = 'No file'
        
        # If file exists, process
        if not rejected:
            data = []
            stream = codecs.iterdecode(uploaded.stream, 'utf-8')
            header = True
            for row in csv.reader(stream, dialect=csv.excel):
                # To skip header
                if header:
                    header = False
                    continue

                # If row is not a comment check if valid
                if row[0][0] != '#':
                    if util.isValidRow(row):
                        data.append(row)
                    else:
                        rejected = True
                        rejectedReason = row
                        break
            
            # If no data extracted from file, reject
            if len(data) == 0 and rejectedReason == '':
                rejected = True
                rejectedReason = 'Empty file'

            # Check if id or login appears twice
            if not rejected:
                columns = [[], []]
                for row in data:
                    columns[0].append(row[0])
                    columns[1].append(row[1])
                if util.isDuplicated(columns[0]) or util.isDuplicated(columns[1]):
                    rejected = True
                    rejectedReason = 'Duplicate Id/Login'
            columns = []

            # Check if any login change that belongs to another user
            if not rejected:
                currLoginList = db.getAllEmployeeLogins()
                for row in data:
                    for login in currLoginList:
                        if row[1] == login[1] and row[0] != login[0]:
                            rejected = True
                            rejectedReason = row
                            break
            
            # If data okay, insert or replace employees
            if not rejected:
                if db.insertEmployees(data):
                    return jsonify({ 'results': 'Upload succeeded' }), 200
                else:
                    return jsonify({ 'results': 'Upload failed' }), 500

        return jsonify({ 'results': 'Rejected due to: ' + str(rejectedReason) }), 400
    except Exception as e:
        print(e)
        return jsonify({ 'results': 'Exception ocurred' }), 500
    finally:
        db.close()
        inUse = False

######################################################
# Run server

if __name__ == '__main__':
    app.run()