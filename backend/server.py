from flask import Flask, request, Response
from database import DatabaseUtil

import csv
import codecs

app = Flask(__name__)
inUse = False

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

        return Response('Rejected: ' + str(rejectedReason), status=400, mimetype='application/json')
    except Exception as e:
        print(e)
        return Response('Rejected: Exception ocurred', status=500, mimetype='application/json')
    finally:
        inUse = False

if __name__ == '__main__':
    app.run()