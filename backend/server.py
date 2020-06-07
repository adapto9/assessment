from flask import Flask, request, Response, jsonify
from database import DatabaseUtil

import csv
import codecs

######################################################
# Globals

app = Flask(__name__)
inUse = False

######################################################
# Helper functions

def isValidRow(row):
    # If not 4 columns, reject
    if len(row) != 4: return False

    # If id or login is not alphanumeric, reject
    if not row[0].isalnum() or not row[1].isalnum(): return False

    # If salary is not decimal or below 0, reject
    try:
        sal = float(row[3])
        if sal < 0: return False
    except ValueError:
        return False

    return True

def isNone(val):
    if val == None: return True
    return False

def isValidParams(minSal, maxSal, offset, limit, sort):
    # If param empty, reject
    if isNone(minSal) or isNone(maxSal) or isNone(offset) or isNone(limit) or isNone(sort) or sort == '':
        return False
    
    # If salary params invalid, reject
    if minSal < 0 or maxSal < 0 or maxSal < minSal:
        return False
    
    # If sort sign not valid, reject
    if sort[0] != '-' and sort[0] != ' ' and sort[0:3] != '%2B':
        return False
    
    # if sort key not valid, reject
    keys = ['id', 'name', 'login', 'salary']
    if sort[0:3] == '%2B':
        if sort[3:] not in keys:
            return False
    else:
        if sort[1:] not in keys:
            return False

    return True

def prepareParams(minSal, maxSal, offset, limit, sort):
    params = None
    sorting = ""
    # If sort sign is URI encoded +
    if sort[0:3] == '%2B':
        params = (minSal, maxSal, limit, offset)
        sorting = sort[3:] + ' ASC'
    else:
        # If sort sign is -
        if sort[0] == '-':
            params = (minSal, maxSal, limit, offset)
            sorting = sort[1:] + ' DESC'
        # If sort sign is + replaced with space
        else:
            params = (minSal, maxSal, limit, offset)
            sorting = sort[1:] + ' ASC'
    return params, sorting

######################################################
# Routes

@app.route('/users', methods = ['GET'])
def getUsers():
    # Validation for request params
    minSal = request.args.get('minSalary', type=float)
    maxSal = request.args.get('maxSalary', type=float)
    offset = request.args.get('offset', type=int)
    limit = request.args.get('limit', type=int)
    sort = request.args.get('sort', type=str)

    if not isValidParams(minSal, maxSal, offset, limit, sort):
        return Response('Param missing', status=400, mimetype='application/json')
    else:
        try:
            params, sorting = prepareParams(minSal, maxSal, offset, limit, sort)
            db = DatabaseUtil()
            res = { 'result': db.getEmployeeDashboard(params, sorting) }
            return jsonify(res), 200
        except Exception as e:
            print(e)
            db.close()
            return Response('Rejected: Exception ocurred', status=500, mimetype='application/json')


@app.route('/users/upload', methods = ['POST'])
def upload():
    global inUse
    if inUse:
        return Response('Rejected: Another file is currently being uploaded', status=503, mimetype='application/json')
    try:
        inUse = True
        # Init
        db = DatabaseUtil()
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
            for row in csv.reader(stream, dialect=csv.excel):
                # If row is not a comment check if valid
                if row[0][0] != '#':
                    if isValidRow(row):
                        data.append(row)
                    else:
                        rejected = True
                        rejectedReason = row
                        break
            
            # If no data extracted from file, reject
            if len(data) == 0 and rejectedReason == '':
                rejected = True
                rejectedReason = 'Empty file'

            # Check if any login change that belongs to another user
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
                    return Response('Upload succeeded', status=200, mimetype='application/json')
                else:
                    return Response('Upload failed', status=500, mimetype='application/json')

        return Response('Rejected: ' + str(rejectedReason), status=400, mimetype='application/json')
    except Exception as e:
        print(e)
        return Response('Rejected: Exception ocurred', status=500, mimetype='application/json')
    finally:
        db.close()
        inUse = False

######################################################
# Run server

if __name__ == '__main__':
    app.run()