import requests

url = 'http://127.0.0.1:5000/users'

def testGetEmployees(minSalary, maxSalary, offset, limit, sort, code):
    params = { 'minSalary': minSalary, 'maxSalary': maxSalary, 'offset': offset, 'limit': limit, 'sort': sort}
    res = requests.get(url, params=params)
    assert res.status_code == code

def testSuite():
    testGetEmployees(0.0, 5000.0, 0, 30, '+id', 200)
    testGetEmployees(0.0, 5000.0, 0, 30, '-id', 200)
    testGetEmployees(0.0, 5000.0, 0, 30, '+login', 200)
    testGetEmployees(0.0, 5000.0, 0, 30, '-login', 200)
    testGetEmployees(0.0, 5000.0, 0, 30, '+name', 200)
    testGetEmployees(0.0, 5000.0, 0, 30, '-name', 200)
    testGetEmployees(0.0, 5000.0, 0, 30, '+salary', 200)
    testGetEmployees(0.0, 5000.0, 0, 30, '-salary', 200)

    testGetEmployees(0.0, 5000.0, 30, 30, '+id', 200)
    testGetEmployees(0.0, 5000.0, 30, -30, '+id', 400)
    testGetEmployees(0.0, 5000.0, -30, 30, '+id', 400)
    testGetEmployees(0.0, 5000.0, -30, -30, '+id', 400)

    testGetEmployees(10.0, 5000.0, 0, 30, '+id', 200)
    testGetEmployees(10.0, 5000, 0, 30, '+id', 200)
    testGetEmployees(10, 5000.0, 0, 30, '+id', 200)
    testGetEmployees(10, 5000, 0, 30, '+id', 200)

    testGetEmployees(0.0, -5000.0, 0, 30, '+id', 400)
    testGetEmployees(-0.0, 5000.0, 0, 30, '+id', 200)
    testGetEmployees(-10.0, 5000.0, 0, 30, '+id', 400)
    testGetEmployees(-0.0, -5000.0, 30, 30, '+id', 400)
    testGetEmployees(-10.0, -5000.0, 30, 30, '+id', 400)
    testGetEmployees(0.0, 0.0, 0, 30, '+id', 200)

    testGetEmployees(0.0, 5000.0, 0, 30, 'id', 400)
    testGetEmployees(0.0, 5000.0, 0, 30, '', 400)
    testGetEmployees(0.0, '5000.0', 0, 30, '+id', 200)
    testGetEmployees(0.0, '5000..0', 0, 30, '+id', 400)
    testGetEmployees(0.0, '5000,0', 0, 30, '+id', 400)
    testGetEmployees('0..0', 5000.0, 0, 30, '+id', 400)
    testGetEmployees('0,0', 5000.0, 0, 30, '+id', 400)
    
    print('Test cases ran successfully!')

testSuite()